"""
Wake word detection module for activating the assistant.

This module is responsible for detecting activation phrases
in user speech input using fuzzy string matching.

It allows flexibility in recognition by tolerating variations
and minor transcription errors through similarity scoring.

The wake word check determines when the assistant should
switch from passive listening to active command mode.
"""

from rapidfuzz import fuzz

WAKE_WORDS = ["spirit", "hey spirit"]
SIMILARITY_THRESHOLD = 90


def is_wake_word(text):

    similarity = max(fuzz.partial_ratio(w, text.lower()) for w in WAKE_WORDS)
    return similarity >= SIMILARITY_THRESHOLD
