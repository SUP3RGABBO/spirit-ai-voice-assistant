"""
Text-to-Speech (TTS) engine for voice output generation.

This module is responsible for converting text into spoken audio
and playing it through the configured audio device.

It supports two execution modes:
- synchronous speech playback for immediate responses
- asynchronous queued speech processing for non-blocking output

The audio pipeline uses:
- gTTS for speech synthesis
- ffmpeg for audio format conversion
- system audio player for output playback

A background worker thread processes queued speech requests
to ensure smooth and non-blocking voice interaction.
"""

import os
import tempfile
import subprocess
import threading
import queue
from gtts import gTTS
from config import SPEAKER_DEVICE


audio_queue = queue.Queue()


def audio_worker():
    while True:
        text = audio_queue.get()
        if text is None:
            break
        try:
            tmp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
            gTTS(text=text, lang="en").save(tmp_mp3)
            tmp_wav = tmp_mp3.replace(".mp3", ".wav")
            subprocess.run(
                ["ffmpeg", "-y", "-i", tmp_mp3, tmp_wav],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            subprocess.run(["aplay", "-D", SPEAKER_DEVICE, tmp_wav])
            os.remove(tmp_mp3)
            os.remove(tmp_wav)
        except Exception as e:
            print("TTS Error:", e)
        audio_queue.task_done()



threading.Thread(target=audio_worker, daemon=True).start()


def speak_async_queue(text):
    audio_queue.put(text)


def speak_text(text):
    try:
        tmp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
        gTTS(text=text, lang="en").save(tmp_mp3)

        tmp_wav = tmp_mp3.replace(".mp3", ".wav")

        subprocess.run(
            ["ffmpeg", "-y", "-i", tmp_mp3, tmp_wav],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        subprocess.run(["aplay", "-D", SPEAKER_DEVICE, tmp_wav])

        os.remove(tmp_mp3)
        os.remove(tmp_wav)

    except Exception as e:
        print("TTS Error:", e)


def speak_async(text):
    threading.Thread(
        target=speak_text,
        args=(text,),
        daemon=True
    ).start()
