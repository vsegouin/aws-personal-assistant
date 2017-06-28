import boto3


class LexRuntimeUtil:
    def __init__(self):
        self.lex_client = boto3.client('lex-runtime')

    def say_something(self):
        response = self.lex_client.post_text(
            botName='TodaysWeather',
            botAlias='inspiration',
            userId='aaa',
            sessionAttributes={'string': 'string'},
            inputText='Say something interresting',
        )
        return response['message']


