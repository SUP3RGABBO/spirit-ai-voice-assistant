"""
Event management and scheduling system for the assistant.

This module is responsible for handling time-based events such as:
- timers
- alarms
- reminders

It continuously monitors active events in a background loop
and triggers actions when conditions are met.

The system integrates:
- persistent memory storage
- voice feedback via TTS
- hardware audio notifications

This acts as the assistant's internal scheduler and time-based engine.
"""

import time
import datetime
import threading
from ai.memory import load_memory, save_memory
from core.tts import speak_text
from hardware.audio_device import play_ringtone


class Events:
    def __init__(self):
        memory = load_memory()

        self.timers = memory.get("timers", [])
        self.alarms = memory.get("alarms", [])
        self.reminders = memory.get("reminders", [])

    def set_timer(self, value, unit):
        if unit.startswith("hour"):
            seconds = value * 3600
        elif unit.startswith("min"):
            seconds = value * 60
        elif unit.startswith("second"):
            seconds = value
        else:
            seconds = value

        end_time = time.time() + seconds
        self.timers.append({"end_time": end_time})
        save_memory(self._export())

        speak_text(f"Timer set for {value} {unit}")

    def set_alarm(self, time_str):
        self.alarms.append({"time": time_str})
        save_memory(self._export())

        speak_text(f"Alarm set for {time_str}")

    def set_reminder(self, text, time_str):
        self.reminders.append({
            "time": time_str,
            "text": text
        })
        save_memory(self._export())

        speak_text(f"Reminder set for {time_str}")

    def _export(self):
        return {
            "timers": self.timers,
            "alarms": self.alarms,
            "reminders": self.reminders
        }

    def check_events(self):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")

            for r in self.reminders[:]:
                if r["time"] == current_time:
                    speak_text(f"Reminder: {r['text']}")
                    self.reminders.remove(r)
                    save_memory(self._export())

            for a in self.alarms[:]:
                if a["time"] == current_time:
                    speak_text("Alarm!")
                    time.sleep(0.8)
                    play_ringtone()
                    self.alarms.remove(a)
                    save_memory(self._export())

            for t in self.timers[:]:
                if time.time() >= t["end_time"]:
                    speak_text("The timer has ended")
                    time.sleep(0.8)
                    play_ringtone()
                    self.timers.remove(t)
                    save_memory(self._export())

            time.sleep(1)
