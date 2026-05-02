import subprocess
from config import RINGTONE_PATH

ringtone_process = None


def play_ringtone(file_path=RINGTONE_PATH):
    global ringtone_process
    if ringtone_process is None or ringtone_process.poll() is not None:
        ringtone_process = subprocess.Popen(
            ["aplay", "-D", "hw:3,0", file_path]
        )


def stop_ringtone():
    global ringtone_process
    if ringtone_process and ringtone_process.poll() is None:
        ringtone_process.terminate()
        ringtone_process = None
