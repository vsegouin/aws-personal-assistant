from utils.ImageUtils import ImageUtils
from utils.Rekognition import Rekognition

image = ImageUtils.encode_img("assets/selfie.jpg")
aw = Rekognition()

facesResponse = aw.detect_face(raw_img=image)
facesResponse = aw.detect_labels(image_raw=image)