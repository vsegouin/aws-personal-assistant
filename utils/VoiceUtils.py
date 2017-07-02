import sys
from contextlib import closing
from tempfile import gettempdir

import boto3
import os
from botocore.exceptions import BotoCoreError, ClientError
from pydub import AudioSegment
# from utils.Rekognition import Rekognition
from utils.audio import Player


class VoiceUtils:
    def __init__(self):
        self.polly_client = boto3.client('polly')
        self.polly_configuration = "Emma"
        self.player = Player()
        #  pygame.mixer.init()

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
                output = os.path.join(gettempdir(), "speech.wav",)

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
        sound.export(os.path.join(gettempdir(), "speech.wav"), format="wav")
        player = Player()
        player.play_wav(gettempdir() + "/speech.wav")

    def fetch_raw(self, text_to_tell):
        try:
            # Request speech synthesis
            response = self.polly_client.synthesize_speech(Text=text_to_tell, OutputFormat="pcm",
                                                           VoiceId=self.polly_configuration,   SampleRate= "16000")
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
            result = '';
            with closing(response["AudioStream"]) as stream:
                result = stream.read()
            print(result)
            return result

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

    def play_sound(self,sound_raw):
        # Play the audio using the platform's default player
        self.player.play_bytes(sound_raw, 16000)

    def describe_face(self,response):
        if len(response['FaceDetails']) > 0:
            numOfFace = len(response['FaceDetails']);
            message = "I'm currently seeing "+repr(numOfFace)+' face, '
            index = 1
            for face in response['FaceDetails']:
                sex = face['Gender']['Value']
                eyeglass = face['Eyeglasses']['Value']
                emotion = face['Emotions'][0]['Type']
                smile = face['Smile']['Value']
                prefix = 'He' if sex == 'Male' else 'Female'

                message += 'The person number '+repr(index)+' is a '+sex+'. '
                if eyeglass:
                    message += prefix+' wears eyeglasses. '
                else :
                    message += prefix+' doesn\'t wear eyeglasses. '
                if smile:
                    message+= prefix+' is smiling. '
                else :
                    message+= prefix+' is not smiling. '
                message+= prefix+' seems to be '+emotion+'. '
        else:
            message = "I'm sorry, i can't detect any face"
        print(message)
        self.tell_me(message)

    def describe_theme(self,response):
        if len(response['Labels']) > 0:
            message = 'I can tell '+repr(len(response['Labels']))+' themes about what I see. '
            for label in response['Labels']:
                message += label['Name']+', '
        else:
            message = "I'm sorry i can't detect any theme about what I see"
        print(message)
        self.tell_me(message)