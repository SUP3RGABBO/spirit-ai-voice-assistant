"""
Speech-to-text module for voice input processing.

This module handles audio capture from the microphone and converts
spoken language into text using speech recognition services.

It provides two main modes:
- activation listening (short, low-latency detection)
- command listening (longer user input processing)

The recognizer is tuned for real-time interaction with optimized
thresholds to reduce noise sensitivity and improve responsiveness.

It also handles network and recognition errors gracefully,
ensuring the assistant remains stable during voice interaction.
"""

import speech_recognition as sr
from config import MIC_INDEX
from core.tts import speak_async_queue


recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = False
recognizer.pause_threshold = 1.6
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 1.2


def listen_for_activation():
    try:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            print("🎤 Listening for activation...")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=4)

        return recognizer.recognize_google(audio, language="en-US")

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        speak_async_queue("I can't connect to voice services. Please check your network.")
        return ""

    except Exception as e:
        print("Activation listening error:", e)
        return ""


def listen_for_command():
    try:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            print("🎤 Listening for command...")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=12)

        return recognizer.recognize_google(audio, language="en-US")

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        speak_async_queue("I can't connect to voice services. Please check your network.")
        return ""

    except Exception as e:
        print("Command listening error:", e)
        return ""
