"""
Simple logging utility for voice interaction tracking.

This module handles persistent logging of assistant interactions
by appending text entries to a log file.

It is mainly used for:
- debugging voice interactions
- tracking conversation history
- storing lightweight runtime logs for later analysis
"""

import os
from config import LOG_FILE

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def append_to_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")