from utils.VoiceUtils import VoiceUtils
from utils.RecordingUtil import RecordingUtil
from utils.LexRuntimeUtil import LexRuntimeUtil
from utils.CameraUtils import PiCamUtils
from utils.Rekognition import Rekognition
import time

if (__name__ == '__main__'):
    lex = LexRuntimeUtil()
    lex.start_vocal_speech()

