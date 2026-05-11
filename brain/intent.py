"""
Simple rule-based intent recognition module.

This module classifies user input into predefined intents
using lightweight regex pattern matching.

It acts as the first step of the NLP pipeline and determines
which system component should handle the request.

The approach is heuristic-based and designed for fast
real-time voice interaction rather than deep language understanding.
"""

import re


def recognize_intent(text):
    text = text.lower()

    if re.search(r"\btimer\b", text):
        return "set_timer"
    elif re.search(r"\balarm\b", text):
        return "set_alarm"
    elif re.search(r"\bremind me\b|\breminder\b", text):
        return "set_reminder"
    elif re.search(r"\bweather\b", text):
        return "weather"
    elif re.search(r"\bvolume\b|\braise\b|\blower\b", text):
        return "manage_volume"
    elif re.search(r"\bstop\b", text):
        return "stop_ringtone"
    elif re.search(r"\btime\b|\bhour\b", text):
        return "current_time"
    else:
        return "chatgpt"
