"""
Extracts structured entities from natural language input.

This module processes user text based on the detected intent
and extracts relevant parameters needed for command execution.

It uses a hybrid approach combining:
- spaCy NLP for linguistic processing
- regex patterns for structured data extraction
- heuristic rules for fallback handling

The extracted entities are used by the command handler
to execute actions such as timers, alarms, reminders, and weather queries.
"""

import re
import spacy
from services.weather import extract_city


nlp = spacy.load("en_core_web_sm")


def extract_entities(text, intent):
    entities = {}
    doc = nlp(text)

    if intent == "set_timer":
        match = re.search(r"(\d+)\s*(seconds|second|minutes|minute|hours|hour)", text)
        if match:
            entities["value"] = int(match.group(1))
            entities["unit"] = match.group(2)
        else:
            entities["value"] = 1
            entities["unit"] = "minutes"

    elif intent == "set_alarm":
        for token in text.split():
            if ":" in token:
                entities["time"] = token
                break
        else:
            entities["time"] = "07:00"  # default

    elif intent == "set_reminder":
        match = re.search(r"at (\d{1,2}:\d{2})", text)
        if match:
            entities["time"] = match.group(1)
            entities["message"] = re.sub(
                r"(remind me|could you remind me)\s*at \d{1,2}:\d{2}",
                "",
                text
            ).strip()
        else:
            entities["time"] = "12:00"
            entities["message"] = re.sub(
                r"(remind me|could you remind me)",
                "",
                text
            ).strip()

    elif intent == "weather":
        entities["city"] = extract_city(text)

    elif intent == "current_time":
        pass

    return entities
