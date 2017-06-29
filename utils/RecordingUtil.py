import numpy
import pyaudio
import analyse

# Initialize PyAudio
pyaud = pyaudio.PyAudio()

device_index = 2
CHANNELS = 1
AUDIO_SAMPLING_RATE = 48000
AUDIO_BUFFER_SIZE = 1024
FORMAT=pyaudio.paInt16

# Open input stream, 16-bit mono at 48000 Hz
# On my system, device 4 is a USB camera

stream = pyaud.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=AUDIO_SAMPLING_RATE,
    input=True,
    frames_per_buffer=AUDIO_BUFFER_SIZE,
    input_device_index=device_index
)
while True:
    # Read raw microphone data
    rawsamps = stream.read(1024)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    # Show the volume
    print(analyse.loudness(samps))
