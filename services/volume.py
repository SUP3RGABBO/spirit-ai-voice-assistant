"""
System volume control utility for the assistant.

This module provides simple functions to adjust system audio volume
using low-level OS audio controls (ALSA via amixer).

It supports:
- increasing volume in fixed steps
- decreasing volume in fixed steps

It is used by voice commands to allow hands-free audio control
of the system output level.
"""

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
