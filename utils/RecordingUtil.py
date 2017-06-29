import wave
import random
import struct
import numpy
import math
import pyaudio
import analyse

# Initialize PyAudio
pyaud = pyaudio.PyAudio()

device_index = 2
CHANNELS = 1
AUDIO_SAMPLING_RATE = 48000
AUDIO_BUFFER_SIZE = 8192
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
sampleRate = 44100.0 # hertz
duration = 1.0       # seconds
frequency = 440.0    # hertz

wavef = wave.open('sound.wav','w')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

for i in range(int(duration * sampleRate)):
    value = int(32767.0*math.cos(frequency*math.pi*float(i)/float(sampleRate)))
    data = struct.pack('<h', value)
    wavef.writeframesraw( data )

wavef.writeframes('')
wavef.close()

while True:
    # Read raw microphone data
    rawsamps = stream.read(1024)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    # Show the volume
    print(analyse.loudness(samps))
