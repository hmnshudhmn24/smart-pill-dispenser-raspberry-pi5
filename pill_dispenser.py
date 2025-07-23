import time
import threading
import RPi.GPIO as GPIO
from datetime import datetime

# GPIO Pins for each pill compartment
PILL_MOTORS = {
    "morning": 17,
    "afternoon": 27,
    "evening": 22
}

# Reminder times
REMINDER_TIMES = {
    "morning": "08:00",
    "afternoon": "13:00",
    "evening": "19:00"
}

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in PILL_MOTORS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def dispense_pill(time_slot):
    pin = PILL_MOTORS[time_slot]
    print(f"Dispensing {time_slot} pills...")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    print(f"{time_slot.capitalize()} pills dispensed!")

def reminder_loop():
    while True:
        now = datetime.now().strftime("%H:%M")
        for slot, remind_time in REMINDER_TIMES.items():
            if now == remind_time:
                print(f"Reminder: Time to take your {slot} pills!")
                dispense_pill(slot)
                time.sleep(60)  # avoid double trigger within the same minute
        time.sleep(30)

def cleanup():
    GPIO.cleanup()
    print("GPIO cleanup done.")

def start_dispenser():
    try:
        print("💊 Smart Pill Dispenser started.")
        reminder_thread = threading.Thread(target=reminder_loop)
        reminder_thread.daemon = True
        reminder_thread.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")
        cleanup()

if __name__ == "__main__":
    start_dispenser()