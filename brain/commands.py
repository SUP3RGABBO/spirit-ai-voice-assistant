from brain.intent import recognize_intent
from brain.entities import extract_entities
from hardware.audio_device import stop_ringtone
from services.weather import get_weather
from services.volume import increase_volume, decrease_volume
from services.time_service import tell_time
from core.tts import speak_text


def handle_voice_command(text, events):
    text = text.lower()
    intent = recognize_intent(text)
    entities = extract_entities(text, intent)

    if intent == "stop_ringtone":
        stop_ringtone()
        speak_text("Okay")
        return True

    elif intent == "set_timer":
        events.set_timer(entities["value"], entities["unit"])
        return True

    elif intent == "set_alarm":
        events.set_alarm(entities["time"])
        return True

    elif intent == "set_reminder":
        events.set_reminder(entities["text"], entities["time"])
        return True

    elif intent == "weather":
        response = get_weather(entities["city"])
        speak_text(response)
        return True

    elif intent == "manage_volume":
        if "increase" in text:
            increase_volume()
            speak_text("Volume increased")
        elif "decrease" in text:
            decrease_volume()
            speak_text("Volume decreased")
        return True

    elif intent == "current_time":
        tell_time()
        return True

    return False
