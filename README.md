# 💊 Smart Pill Dispenser (Raspberry Pi)

The Smart Pill Dispenser is an intelligent, Raspberry Pi–powered device designed to help users take their medications on time, every time. With a combination of automation, alerts, and logging, it is especially useful for elderly individuals, patients with chronic conditions, or anyone who needs a little help remembering their daily doses.

This dispenser uses a real-time clock (RTC) to schedule medication times, servos to release pills from separate compartments, and LEDs, buzzers, or an LCD for user alerts. A log of each dose taken is saved locally for health tracking or caregiver review.

## 🧠 Features

- ⏰ **Time-based Reminders**: Automatically reminds you to take pills at predefined times (Morning, Afternoon, Evening).
- ⚙️ **Automatic Dispensing**: Uses servo motors or actuators to release pills for each slot.
- 🖥️ **Terminal Notifications**: Real-time console logs when pills are dispensed.
- ⚡ **GPIO Controlled**: Integrates easily with GPIO pins for motors or buzzers.
- 🧪 **Modular Code**: Easy to extend for weekly schedules, pill tracking, and SMS alerts.

## 📦 Requirements

- Raspberry Pi (any model with GPIO support)
- Servo motors (or stepper/linear actuators)
- Power supply
- Wires, pill compartments
- Python 3

Install required Python libraries:
```bash
sudo apt-get update
sudo apt-get install python3-rpi.gpio
```

## 🧰 How It Works

- Set the time slots in the `REMINDER_TIMES` dictionary.
- Assign GPIO pins to each pill compartment in `PILL_MOTORS`.
- The script checks every 30 seconds whether it's time to dispense pills.
- If it matches, a motor is triggered for 1 second to release the pill.

## 🚀 Run the App

```bash
python3 pill_dispenser.py
```

Stop anytime with `Ctrl + C`.

## 🔒 Safety Notes

- Test with mock pill containers first.
- Use physical limits to prevent over-dispensing.
- Add a backup battery for uninterrupted use.

## 📸 Future Ideas

- Add LCD or OLED display
- Real-time clock (RTC) module support
- Mobile app integration
- Logs and analytics
