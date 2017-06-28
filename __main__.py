from utils.LexRuntimeUtil import LexRuntimeUtil
from utils.VoiceUtils import VoiceUtils


lr = LexRuntimeUtil()
vu = VoiceUtils()

vu.tell_me(lr.say_something())
