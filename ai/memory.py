"""
Manages persistent memory storage for the assistant.

This module is responsible for:
- loading and initializing memory from disk
- saving updated memory state
- storing conversation history with timestamps
- providing recent conversation context for the AI

Memory is stored in a JSON file and is used to give the assistant
continuity across sessions (e.g., reminders, alarms, and chat history).
"""

import os
import json
import datetime
from config import MEMORY_FILE


os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "timers": [],
            "alarms": [],
            "reminders": [],
            "conversations": []
        }

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "conversations" not in data:
                data["conversations"] = []
            return data
    except Exception as e:
        print("Memory loading error:", e)
        return {
            "timers": [],
            "alarms": [],
            "reminders": [],
            "conversations": []
        }


def save_memory(data):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print("Memory saving error:", e)


def add_conversation_memory(user_text, assistant_text):
    memory = load_memory()
    memory["conversations"].append({
        "user": user_text,
        "assistant": assistant_text,
        "timestamp": datetime.datetime.now().isoformat()
    })
    save_memory(memory)


def get_conversation_memory(limit=5):
    """Retrieve the last limit conversations for context"""
    memory = load_memory()
    return memory["conversations"][-limit:]
