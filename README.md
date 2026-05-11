# Spirit AI Voice Assistant

A modular AI voice assistant built with Python and Raspberry Pi, featuring real-time speech recognition, ChatGPT integration, wake word detection, hardware interaction, and event management.



## Features

- Real-time voice interaction
- Wake word detection system
- Speech-to-text recognition
- Text-to-speech responses
- ChatGPT integration with streaming responses
- Intent recognition and entity extraction
- Timers, alarms, and reminders
- Weather information service
- Conversation memory system
- LED hardware feedback
- Raspberry Pi audio integration
- Modular architecture for scalability

## Architecture

The project is organized into independent modules to keep the assistant scalable, maintainable, and easy to expand.

- `main.py` → Entry point of the assistant
- `config.py` → Global configuration, API keys, device setup

- `core/` → Speech recognition, text-to-speech, wake word detection, logging
- `ai/` → ChatGPT integration, prompts, conversation memory
- `brain/` → Intent recognition, entity extraction, command handling
- `services/` → Timers, alarms, reminders, weather, system utilities
- `hardware/` → Raspberry Pi hardware control (LEDs, audio devices)
- `data/` → Runtime-generated memory and logs
- `sounds/` → Audio files (ringtone and sound effects)


## Hardware Requirements

The assistant was developed and tested using the following hardware configuration:

- Raspberry Pi 4 Model B (8GB RAM)
- reSpeaker XMOS XVF3800 AI-powered 4-Microphone Array
- USB stereo speaker
- Argon ONE case for Raspberry Pi 4
- Custom 3D-printed shell and decorative components

The external shell and decorative elements were designed using FreeCAD and Blender, then printed and manually assembled.  
The structure was painted using solvent-based spray paint to achieve a more industrial finish.

The project can also work with different microphones and speakers, but audio device indexes and configuration parameters may need to be adjusted inside the project settings.

## Software Requirements

The assistant was developed and tested on Raspberry Pi OS using Python 3.

Required software and tools:

- Python 3.10+
- ffmpeg
- ALSA audio system
- OpenAI API access
- Internet connection for speech recognition and AI responses

Python dependencies are listed inside the `requirements.txt` file.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Spirit-AI-Voice-Assistant.git
```

Move into the project folder:

```bash
cd Spirit-AI-Voice-Assistant
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Sounds Setup

The project uses a `sounds/` directory to store audio files such as the ringtone used for alarms and timers.

If the folder does not exist, you must create it manually in the root directory of the project:

```bash
mkdir sounds
```
Then place your desired audio file inside this folder.
The system expects the ringtone file to be located at:
RINGTONE_PATH = os.path.join(BASE_DIR, "sounds", "ringtone.wav")
You can replace this file with any custom sound, as long as the filename and format match the configuration in config.py.


## Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:

```env
OPENAI_API_KEY=your_openai_key_here
WEATHER_API_KEY=your_weather_key_here
```

The OpenAI API key is required for ChatGPT responses, while the weather API key is used for real-time weather information.

## Raspberry Pi Setup

This project was developed and tested on a Raspberry Pi 4 Model B (8GB) using the official 64-bit Raspberry Pi OS installed via Raspberry Pi Imager.

### System Setup

The following system-level dependencies are required for proper functionality:

- ffmpeg installed via system package manager
- ALSA audio system configured for default input/output devices
- USB audio routing configured for microphone and speaker recognition
- Python virtual environment recommended for dependency isolation

### Audio Configuration

Audio input and output are handled through ALSA.  
The system uses device indexing defined inside the configuration file to select the correct microphone and speaker.

Manual ALSA configuration was performed to ensure stable default routing for both USB microphone input and USB speaker output.
Ensure that audio device indexes defined in `config.py` match your hardware configuration.
### Speech Recognition Dependencies

The voice recognition system relies on:

- PortAudio
- PyAudio
- SpeechRecognition library

These were installed at system level to enable microphone access and real-time audio processing.

### reSpeaker Microphone Setup

The system uses a reSpeaker XMOS XVF3800 microphone array.

Device-specific drivers and tools were installed following the official Seeed Studio documentation.  
The provided `xvf_host` utility is included in the project and used for controlling hardware features such as LED effects.

### Audio Output

Audio playback is handled using system utilities such as:

- `aplay`
- `amixer`

These are used for routing and controlling speaker output on the configured audio device.

### LED Control

LED behavior is managed through the reSpeaker firmware interface and controlled via the `xvf_host` tool.  
The Python project interacts with this tool to trigger visual feedback during wake word detection and system events.

## Run the Assistant

After completing the installation and configuration steps, start the assistant with:

```bash
python main.py
```

The system will initialize all modules, activate the wake word listener, and start the voice interaction loop.

To stop the assistant, use `CTRL + C` in the terminal.

### Running via SSH (optional)

If running the assistant remotely via SSH and you want it to continue running after closing the session, you can use:

```bash
nohup python main.py &
```

Alternatively, you can use `tmux` or `screen` for better session management.

## Possible Extensions

This project is considered complete in its current form.  
However, it can be extended in the future with additional features such as:

- Improved wake word detection using dedicated ML models
- Extended smart home integrations
- Web-based control dashboard
- Advanced long-term memory system
- Additional hardware sensor support


## Security Note

This project runs locally on Raspberry Pi and executes system-level commands for audio and hardware control.  
It does not expose any network services or remote access interfaces.

## Author

Developed by Gabriele Giovinazzo.

## Links

YouTube Channel: https://youtube.com/@gabriele_giovinazzo

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software with attribution.