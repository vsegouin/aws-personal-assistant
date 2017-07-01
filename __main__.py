from utils.VoiceUtils import VoiceUtils
from utils.RecordingUtil import RecordingUtil
from utils.LexRuntimeUtil import LexRuntimeUtil
from utils.CameraUtils import PiCamUtils
from utils.Rekognition import Rekognition
import time

if (__name__ == '__main__'):
    # listen_for_speech()  # listen to mic.
    # print(stt_google_wav('hello.flac')  # translate audio file)
    # audio_int()  # To measure your mic levels

    #   vu = VoiceUtils()
    #  ru = RecordingUtil()
    lex = LexRuntimeUtil()
    lex.start_vocal_speech()

