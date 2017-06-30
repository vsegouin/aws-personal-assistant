from contextlib import closing

import boto3

from utils.VoiceUtils import VoiceUtils


class LexRuntimeUtil:
    def __init__(self):
        self.lex_client = boto3.client('lex-runtime')
        self.voice_client = VoiceUtils()

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
            totot = input('toto')
            response = self.lex_client.post_content(
                botName='WeatherInWorld',
                botAlias='TodayWeather',
                userId='aaa',
                sessionAttributes={},
                contentType='audio/l16; rate=16000; channels=1',
                accept='audio/pcm',
                inputStream=totot
            )
            if "audioStream" in response:
                result = '';
                with closing(response["audioStream"]) as stream:
                    message = stream.read()
                print(message)

        return message


