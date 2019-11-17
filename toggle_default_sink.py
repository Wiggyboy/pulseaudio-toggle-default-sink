# 
# Copyright 2019 (C) Wiggy boy <Lindholm>
# (formally known as Osvald Lindholm)
#

# This will toggle through the audio sinks defined in audio-sinks.py
# and set the toggled audio sink as default audio sink for PulseAudio.

from sys import argv
from audio_sinks import audio_sinks
default_sink_file = "default-sink.tmp"

# Get current default sink (index)
try:
    with open(default_sink_file, 'r') as f:
        sink_index = int(f.read())

except (OSError, ValueError):
    # Could either not open/read the file,
    # or not interpret the data as an int.
    # Either way assume ...
    sink_index = 0

# Toggle either forward/backwards with next/prev.
# If no input or faulty input is given,
# just redo the set of current default sink.

if (len(argv) > 1):
    toggle_operation = argv[1]

    if (toggle_operation == "next"):
        sink_index += 1
    elif (toggle_operation == "prev" or toggle_operation == "previous"):
        sink_index -= 1

# Ensure sink_index is within the indicies of audio_sinks
sink_index = sink_index % len(audio_sinks)


# TODO set default sink


# Save current default sink (index)
try:
    with open(default_sink_file, 'w') as f:
        f.write(str(sink_index))

except OSError:
    # TODO handle this error properly
    pass


