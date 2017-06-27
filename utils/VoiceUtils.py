from contextlib import closing
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from utils.Rekognition import Rekognition
import pygame, StringIO
import sys, traceback


class VoiceUtils:
    def __init__(self):
        self.polly_client = boto3.client('polly')
        self.polly_configuration = "Emma"
        pygame.mixer.init()

    def tell_me(self, text_to_tell):
        try:
            # Request speech synthesis
            print('Try to get text')
            response = self.polly_client.synthesize_speech(Text=text_to_tell, OutputFormat="ogg_vorbis",
                                                           VoiceId=self.polly_configuration)
        except (BotoCoreError, ClientError) as error:
            # The service returned an error, exit gracefully
            print(error)
            sys.exit(-1)

        # Access the audio stream from the response
        if "AudioStream" in response:
            # Note: Closing the stream is important as the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
            print('Speech got')
            with closing(response["AudioStream"]) as stream:
                print("reading data")
                data = stream.read()
                print("writing text")
                filelike = StringIO.StringIO(data)  # Gives you a file-like object
                sound = pygame.mixer.Sound(file=filelike)
                sound.set_volume(100)
                print('playing sound')
                sound.play()
                while pygame.mixer.get_busy() == True:
                    continue


        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio")
            sys.exit(-1)

    def list_languages(self, language):
        r_voices = self.polly_client.describe_voices(
            LanguageCode=language
        )
        for voice in r_voices['Voices']:
            print(voice)
            print(voice['Id'])

    def what_this_image_about(self, raw_img):
        response = Rekognition().detect_labels(raw_img)
        sujet = response['Labels'][0]["Name"]
        self.tell_me("This image is about " + sujet)
