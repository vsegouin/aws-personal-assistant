import pyaudio
import wave
from utils.VoiceUtils import VoiceUtils
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "apt.wav"

    p = pyaudio.PyAudio()

    print(p.get_device_count())
    print(p.get_device_info_by_index(0))
    print(p.get_device_info_by_index(1))
    print(p.get_device_info_by_index(2))
    print(p.get_device_info_by_index(3))
    print(p.get_device_info_by_index(4))
    print(p.get_device_info_by_index(5))
    stream = p.open(format=pyaudio.paInt16,
                    rate=48000,
                    channels=1,  # change this to what your sound card supports
                    input_device_index=2,  # change this your input sound card index
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
    p.terminate()
    return b''.join(frames)

record_audio()
frams = record_audio()
vu = VoiceUtils()
vu.play_sound(frams)