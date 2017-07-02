from contextlib import closing
from utils.RecordingUtil import RecordingUtil
import boto3
import audioop
from utils.VoiceUtils import VoiceUtils
from utils.CameraUtils import PiCamUtils
from utils.Rekognition import Rekognition
import random

class LexRuntimeUtil:
    def __init__(self):
        self.lex_client = boto3.client('lex-runtime')
        self.voice_client = VoiceUtils()
        self.recorder = RecordingUtil()
        self.camera = PiCamUtils()
        self.rekognition = Rekognition()

    def start_discussion(self):
        dialogState = ''
        message = 'What do you want ?'
        while dialogState == '' or dialogState == 'ElicitSlot' or dialogState == 'ElicitIntent':
            inputText = input(message)
            response = self.lex_client.post_text(
                botName='WeatherInWorld',
                botAlias='TodayWeather',
                userId='aaa',
                sessionAttributes={},
                inputText=inputText,
            )
            dialogState = response['dialogState']
            print(response)
            message = response['message']
        return message

    def start_speech(self,voice):
        dialogState = ''
        message = 'What do you want ?'
        while dialogState == '' or dialogState == 'ElicitSlot' or dialogState == 'ElicitIntent':
            inputText = input(message)
            response = self.lex_client.post_content(
                botName='WeatherInWorld',
                botAlias='TodayWeather',
                userId='aaa',
                sessionAttributes={},
                contentType='audio/l16; rate=16000; channels=1',
                accept='audio/pcm',
                inputStream=voice
            )
            print(response)
            dialogState = response['dialogState']
            message = response['message']
        return message

    def start_vocal_speech(self):
        dialogState = 'ElicitIntent'
        userId = repr(random.randrange(0,100000))
        self.voice_client.tell_me('What do you want ?')
        while dialogState == 'ElicitSlot' or dialogState == 'ElicitIntent':
            command_to_send = self.recorder.loudness_test()
            response = self.lex_client.post_content(
                botName='WeatherInWorld',
                botAlias='TodayWeather',
                userId=userId,
                sessionAttributes={},
                contentType='audio/l16; rate=16000; channels=1',
                accept='audio/pcm',
                inputStream=command_to_send
            )
            print(response)
            if "audioStream" in response:
                result = '';
                with closing(response["audioStream"]) as stream:
                    message = stream.read()
                self.voice_client.play_sound(message)

            if response['inputTranscript'] == 'start the camera':
                self.camera.start_preview()

            if response['inputTranscript'] == 'stop the camera':
                self.camera.stop_preview()

            if response['inputTranscript'] == 'describe this':
                photo = self.camera.take_screenshot()
                response = self.rekognition.detect_labels(photo,4)

            if response['inputTranscript'] == 'take capture':
                photo = self.camera.take_screenshot()
                response = self.rekognition.detect_face(photo)
                self.voice_client.describe_face(response)

            if "dialogState" in response:
                if response["dialogState"] == "Fulfilled" or response["dialogState"] == "Failed":
                    userId = repr(random.randrange(0,100000))

        return message


