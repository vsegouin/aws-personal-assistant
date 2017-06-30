from contextlib import closing
from utils.RecordingUtil import RecordingUtil
import boto3
import audioop
from utils.VoiceUtils import VoiceUtils


class LexRuntimeUtil:
    def __init__(self):
        self.lex_client = boto3.client('lex-runtime')
        self.voice_client = VoiceUtils()
        self.recorder = RecordingUtil()

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
        dialogState = ''
        prompt = 'What do you want ?'
        message = ''
        self.voice_client.tell_me(prompt)
        while dialogState == '' or dialogState == 'ElicitSlot' or dialogState == 'ElicitIntent':
            command_to_send = self.recorder.record_audio()
            state = None
            command_to_send = audioop.ratecv(command_to_send,1,1,48000,16000,state)

            response = self.lex_client.post_content(
                botName='WeatherInWorld',
                botAlias='TodayWeather',
                userId='aaa',
                sessionAttributes={},
                contentType='audio/l16; rate=16000; channels=1',
                accept='audio/pcm',
                inputStream=command_to_send[0]
            )
            if "audioStream" in response:
                result = '';
                with closing(response["audioStream"]) as stream:
                    message = stream.read()
                print(message)
                self.voice_client.play_sound(message)

        return message


