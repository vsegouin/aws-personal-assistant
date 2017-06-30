from contextlib import closing
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from utils.Rekognition import Rekognition
import pygame, StringIO
import sys, traceback
#from utils.Rekognition import Rekognition
from utils.audio import Player
import utils.speech
from pydub import AudioSegment


class VoiceUtils:
    def __init__(self):
        self.polly_client = boto3.client('polly')
        self.polly_configuration = "Emma"
        pygame.mixer.init()

    def tell_me(self, text_to_tell):
        try:
            # Request speech synthesis
            response = self.polly_client.synthesize_speech(Text=text_to_tell, OutputFormat="mp3",
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
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio")
            sys.exit(-1)

        # Play the audio using the platform's default player
        sound = AudioSegment.from_mp3(output)
        sound.export(gettempdir(), format="wav")
        player = Player()
        player.play_wav(gettempdir() + "speech.wav")

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
        self.tell_me("This image is about ")

