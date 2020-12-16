# 
# Copyright 2019 (C) Wiggy boy <Lindholm>
# (formally known as Osvald Lindholm)
#

# This file we specifies which audio sinks (by name) to toggle through.
# The order of the sinks will the same as the toggle order.

cache_file = "default-sink.tmp"
audio_sinks = [
    # Edit/Add yours sinks here
    #
    # Example of two possible audio sink:
    # 'alsa_output.pci-0000_00_1f.3.analog-stereo',
    # 'alsa_output.pci-0000_01_00.1.hdmi-stereo-extra3',
]

# Do not edit below this line

# Verify audio_sinks is valid
if (len(audio_sinks) == 0):
    from subprocess import getoutput
    from textwrap import dedent

    get_available_audio_sinks_cmd = "pactl list sinks short | grep -o -P '^[0-9]+\\s[A-z0-9\\.\\-\\_]+'"
    available_audio_sinks = list(getoutput(get_available_audio_sinks_cmd).split()[1::2])

    print(dedent("""\
        audio_sinks cannot be empty.

        You probably missed to configure your audio sinks.
        Edit audio_sinks.py to fill in the audio_sinks
        you would like to be able to toggle through.

        Detected possible audio sinks are:
    """) + "\n".join(available_audio_sinks)
    )
    exit(0)
