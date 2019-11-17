# 
# Copyright 2019 (C) Wiggy boy <Lindholm>
# (formally known as Osvald Lindholm)
#

# This will toggle through the audio sinks defined in audio-sinks.py
# and set the toggled audio sink as default audio sink for PulseAudio.

from sys import argv
from subprocess import getoutput, call

from audio_sinks import audio_sinks, cache_file as default_sink_file

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
audio_sink = audio_sinks[sink_index]


# Set the default sink
call("pactl set-default-sink " + audio_sink, shell=True)

# Update/Move the current audio sources to use the new default sink
get_audio_srcs_cmd = "pacmd list-sink-inputs | grep -o -P '(?<=index:\\s)[0-9]+'"
audio_srcs = list(getoutput(get_audio_srcs_cmd).split())

move_audio_srcs_cmds = []
for audio_src in audio_srcs:
    move_audio_srcs_cmds.append("pacmd move-sink-input " + audio_src + " " + audio_sink)

if (len(move_audio_srcs_cmds) > 0):
    move_audio_srcs_cmd = " & ".join(move_audio_srcs_cmds)
    call(move_audio_srcs_cmd, shell=True)

# Save current default sink (index)
try:
    with open(default_sink_file, 'w') as f:
        f.write(str(sink_index))

except OSError:
    # TODO handle this error properly
    pass


