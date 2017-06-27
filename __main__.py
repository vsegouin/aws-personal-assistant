from utils.ImageUtils import ImageUtils
from utils.Rekognition import Rekognition

from utils.ImageUtils import ImageUtils
from utils.Rekognition import Rekognition
from utils.VoiceUtils import VoiceUtils
from utils.CameraUtils import PiCamUtils

import picamera
import time

vu = VoiceUtils()
camera = picamera.PiCamera()
camera.start_preview()
time.sleep(3)
camera.capture('photo.jpg')
image = ImageUtils.encode_img("photo.jpg")
aw = Rekognition()

facesResponse = aw.detect_face(raw_img=image)
print(facesResponse)

vu.tell_me('I see a '+(facesResponse['Gender']['Value'])+' which seems to be '+facesResponse['Emotions'][0]['Type'])