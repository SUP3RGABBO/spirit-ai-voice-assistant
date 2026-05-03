import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Assistant
assistant_name = "Spirit"



# Audio
MIC_INDEX = 2
SPEAKER_DEVICE = "plughw:3,0"



DATA_FOLDER = "data"

LOG_FILE = os.path.join(DATA_FOLDER, "chat_log.txt")
MEMORY_FILE = os.path.join(DATA_FOLDER, "memory.json")

# Hardware
XVF_HOST_PATH = "./reSpeakerXVF_rpi/xvf_host"

# Weather
weather_api_key = os.getenv("WEATHER_API_KEY")
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

# Sounds
import os as _os
BASE_DIR = _os.path.dirname(_os.path.abspath(__file__))
RINGTONE_PATH = _os.path.join(BASE_DIR, "sounds", "ringtone.wav")