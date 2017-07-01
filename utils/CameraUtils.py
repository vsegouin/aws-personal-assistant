import picamera
import time
import io

class PiCamUtils:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.sharpness = 0
        self.camera.contrast = 0
        self.camera.brightness = 50
        self.camera.saturation = 0
        self.camera.ISO = 0
        self.camera.video_stabilization = False
        self.camera.exposure_compensation = 0
        self.camera.exposure_mode = 'auto'
        self.camera.meter_mode = 'average'
        self.camera.awb_mode = 'auto'
        self.camera.image_effect = 'none'
        self.color_effects = None
        self.camera.rotation = 0
        self.camera.hflip = False
        self.camera.vflip = False
        self.camera.crop = (0.0, 0.0, 1.0, 1.0)

    def take_screenshot(self):
        stream = io.BytesIO()

        self.camera.capture(stream, format='jpeg')
        # At this point the image is available as stream.array
        return bytearray(stream.getvalue())

    def start_preview(self):
        self.camera.start_preview()

    def stop_preview(self):
        self.camera.stop_preview()

    def start_recording(self):
        self.camera.start_recording('video.h264')

    def stop_recording(self):
        self.camera.stop_recording()
