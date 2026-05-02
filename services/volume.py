import subprocess


def increase_volume():
    subprocess.run(
        ["amixer", "-c", "3", "set", "PCM", "10%+"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def decrease_volume():
    subprocess.run(
        ["amixer", "-c", "3", "set", "PCM", "10%-"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
