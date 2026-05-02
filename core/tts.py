import os
import tempfile
import subprocess
import threading
import queue
from gtts import gTTS
from config import SPEAKER_DEVICE

# ---------------- AUDIO QUEUE ----------------
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


# Start audio worker thread
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
