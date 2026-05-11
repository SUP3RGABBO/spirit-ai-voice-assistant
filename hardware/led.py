"""
Hardware LED control module for visual feedback.

This module manages LED effects through an external hardware interface,
providing visual indicators for assistant states and events.

It supports:
- setting LED color and brightness
- triggering temporary visual effects
- non-blocking execution using separate processes

It is mainly used to signal system activity such as wake word detection
or assistant activation states.
"""

import time
import subprocess
import multiprocessing
from config import XVF_HOST_PATH


def led_process(duration=5, color="0x0000ff", brightness=200):
    try:
        subprocess.run(["sudo", XVF_HOST_PATH, "led_effect", "1"], check=True)
        subprocess.run(["sudo", XVF_HOST_PATH, "led_color", color], check=True)
        subprocess.run(["sudo", XVF_HOST_PATH, "led_brightness", str(brightness)], check=True)

        time.sleep(duration)

        subprocess.run(["sudo", XVF_HOST_PATH, "led_effect", "0"], check=True)

    except Exception as e:
        print("LED Error:", e)


def led_flash_on_wakeword():
    p = multiprocessing.Process(target=led_process, daemon=True)
    p.start()
