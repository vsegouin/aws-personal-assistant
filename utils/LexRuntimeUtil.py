import boto3


class LexRuntimeUtil:
    def __init__(self):
        self.lex_client = boto3.client('lex-runtime')

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
                contentType='audio/mpeg; rate=22050; channels=1',
                accept='audio/mpeg',
                inputStream=voice
            )
            dialogState = response['dialogState']
            message = response['message']
        return message

