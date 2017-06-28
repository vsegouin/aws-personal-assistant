import boto3


class LexRuntimeUtil:
    def __init__(self):
        self.lex_client = boto3.client('lex-runtime')

    def say_something(self):
        response = self.lex_client.post_content(
            botName='TodaysWeather',
            sessionAttributes= True,
            contentType='string',
            accept='string',
        )

lr = LexRuntimeUtil()
lr.say_something()