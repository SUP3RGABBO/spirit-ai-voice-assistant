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
