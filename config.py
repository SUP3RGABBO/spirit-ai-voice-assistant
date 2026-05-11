"""
Central configuration module for the Spirit AI Voice Assistant.

This file manages all global settings and external integrations including:
- environment variable loading
- OpenAI client initialization
- hardware device configuration (microphone and speaker)
- file system paths for logs and memory
- external API keys and base URLs

It acts as the single source of truth for system-wide configuration,
ensuring consistency across all modules of the assistant.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


assistant_name = "Spirit"




MIC_INDEX = 2
SPEAKER_DEVICE = "plughw:3,0"



DATA_FOLDER = "data"

LOG_FILE = os.path.join(DATA_FOLDER, "chat_log.txt")
MEMORY_FILE = os.path.join(DATA_FOLDER, "memory.json")


XVF_HOST_PATH = "./reSpeakerXVF_rpi/xvf_host"


weather_api_key = os.getenv("WEATHER_API_KEY")
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


import os as _os
BASE_DIR = _os.path.dirname(_os.path.abspath(__file__))
RINGTONE_PATH = _os.path.join(BASE_DIR, "sounds", "ringtone.wav")