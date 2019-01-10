"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys

CHUNK = 1024


# wf = wave.open(sys.argv[1], 'rb') # Original example
wf = your_audio_data_array

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=p.get_format_from_width(your_audio_data_samplewidth),
                channels=your_audio_data_nChannels,
                rate=your_audio_data_framerate,
                output=True)

# read data
data = wf # your_audio_data_array

# play stream (3)
while len(data) > 0:
    stream.write(data)
    # data = wf.readframes(CHUNK) # read more data if you want to stream another buffer

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()
