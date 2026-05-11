"""
Simple time service for voice responses.

This module retrieves the current system time and formats it
into a natural spoken response using the text-to-speech system.

It is used by the assistant to answer time-related queries
in a human-friendly spoken format.
"""

import datetime
from core.tts import speak_text


def tell_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    if minute == 0:
        speak_text(f"It is {hour} o'clock")
    elif minute < 10:
        speak_text(f"It is {hour} oh {minute}")
    else:
        speak_text(f"It is {hour} {minute}")
