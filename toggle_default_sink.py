# 
# Copyright 2019 (C) Wiggy boy <Lindholm>
# (formally known as Osvald Lindholm)
#

# This will toggle through the audio sinks defined in audio-sinks.py
# and set the toggled audio sink as default audio sink for PulseAudio.

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

# TODO set default sink

# Save current default sink (index)
try:
    with open(default_sink_file, 'w') as f:
        f.write(str(sink_index))

except OSError:
    # TODO handle this error properly
    print("Fail to write to file")


