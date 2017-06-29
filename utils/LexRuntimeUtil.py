import boto3


class LexRuntimeUtil:
    def __init__(self):
        self.lex_client = boto3.client('lex-runtime')

    def start_discussion(self):
        dialogState = ''
        message = 'What do you want ?'
        while dialogState == '' or dialogState == 'ElicitSlot' or dialogState == 'ElicitIntent':
            inputText = raw_input(message)
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

    def start_speech(self):
        dialogState = ''
        message = 'What do you want ?'
        while dialogState == '' or dialogState == 'ElicitSlot' or dialogState == 'ElicitIntent':
            inputText = raw_input(message)
            response = self.lex_client.post_content(
                botName='WeatherInWorld',
                botAlias='TodayWeather',
                userId='aaa',
                sessionAttributes={},
                contentType='text/plain; charset=utf-8',
                accept='text/plain; charset=utf-8',
                inputStream=inputText
            )
            dialogState = response['dialogState']
            message = response['message']
        return message

