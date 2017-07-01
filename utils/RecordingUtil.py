import audioop
import math
import struct
import time
from collections import deque

import pyaudio

SHORT_NORMALIZE = (1.0 / 32768.0)


class RecordingUtil:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.slid_win = deque(maxlen=6)
        self.frames = []
        self.recording = True

    def record_audio(self):
        CHUNK = 1024 * 8
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 48000
        RECORD_SECONDS = 5
        INPUT_DEVICE_INDEX = 2
        WAVE_OUTPUT_FILENAME = "apt.wav"

        stream = self.p.open(format=pyaudio.paInt16,
                             rate=48000,
                             channels=1,  # change this to what your sound card supports
                             input_device_index=2,  # change this your input sound card index
                             input=True,
                             output=False,
                             frames_per_buffer=1024 * 8)

        frames = []
        print("* Recording audio...")
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done\n")
        stream.stop_stream()
        stream.close()
        return b''.join(frames)

    def get_rms(self, block):
        """Get root mean square as a measure of loudness"""

        count = len(block) / 2
        format = "%dh" % (count)
        shorts = struct.unpack(format, block)
        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
        sum_squares += n * n
        return math.sqrt(sum_squares / count)

    def callback(self,in_data, frame_count, time_info, status):
        self.slid_win.append((self.get_rms(in_data) * 1000))
        if (sum([x for x in self.slid_win]) / 6) > 0.3:
            self.frames.append((in_data))
        elif len(self.frames) > 0:
            self.recording = False
        return (in_data, pyaudio.paContinue)

    def loudness_test(self):
        self.slid_win = deque(maxlen=6)
        self.frames = []
        self.recording = True
        stream = self.p.open(format=pyaudio.paInt16,
                             rate=48000,
                             channels=1,  # change this to what your sound card supports
                             input_device_index=2,  # change this your input sound card index
                             input=True,
                             output=False,
                             frames_per_buffer=1024 * 8,
                             stream_callback=self.callback)

        print("* Recording audio...")
        stream.start_stream()
        while self.recording:
            time.sleep(0.1)
        print("* done\n")
        stream.stop_stream()
        stream.close()
        state = None
        result = audioop.ratecv(b''.join(self.frames), 1, 1, 48000, 16000, state)

        return result[0]

    def get_source(self):
        return self.p.open(format=pyaudio.paInt16,
                           rate=48000,
                           channels=1,  # change this to what your sound card supports
                           input_device_index=2,  # change this your input sound card index
                           input=True,
                           output=False,
                           frames_per_buffer=1024 * 8)