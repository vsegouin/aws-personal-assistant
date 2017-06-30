import pyaudio

class RecordingUtil :
    def __init__(self):
        self.p = pyaudio.PyAudio()
    def record_audio(self):
        CHUNK = 1024*8
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 48000
        RECORD_SECONDS = 5
        INPUT_DEVICE_INDEX = 2
        WAVE_OUTPUT_FILENAME = "apt.wav"

        stream = self.p.open(format=FORMAT,
                             rate=RATE,
                             channels=CHANNELS,  # change this to what your sound card supports
                             input_device_index=INPUT_DEVICE_INDEX,  # change this your input sound card index
                             input=True,
                             output=False,
                             frames_per_buffer=CHUNK)


        frames = []
        print("* Recording audio...")
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done\n")
        stream.stop_stream()
        stream.close()
        return b''.join(frames)
