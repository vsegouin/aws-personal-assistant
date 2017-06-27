#from utils.ImageUtils import ImageUtils
#from utils.Rekognition import Rekognition

#from utils.ImageUtils import ImageUtils
#from utils.Rekognition import Rekognition
#from utils.CameraUtils import PiCamUtils

#import picamera
#import time

from utils.VoiceUtils import VoiceUtils

#camera = picamera.PiCamera()
#camera.start_preview()
#time.sleep(3)
#camera.capture('photo.jpg')
#image = ImageUtils.encode_img("photo.jpg")
#aw = Rekognition()

#facesResponse = aw.detect_face(raw_img=image)

voice = VoiceUtils()
VoiceUtils.tell_me(voice, "tell me a story")






