import boto3
import os
import subprocess
import sys
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from tempfile import gettempdir
import GoogleImageDownloader

class AwsWrapper:
    def __init__(self):
        self.m_last_image = ""
        self.rekognition_client = boto3.client('rekognition')
        self.polly_client = boto3.client('polly')
        self.polly_configuration = "Emma"
        self.s3_client = boto3.resource('s3')

    def describe_me(self, keyword):
        raw_img = GoogleImageDownloader.get_image_from_google(keyword)
        self.rekognize_image(raw_img)

    def encode_img(self,image_path):
        with open(image_path, "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)
            return b

    def rekognize_image(self, raw_img):
            response = self.rekognition_client.detect_labels(
                Image={
                    'Bytes': raw_img
                },
                MaxLabels=123,
                MinConfidence=60
            )  # Let's use Amazon S3
            print(response)
            self.m_last_image = response
            return response

    def list_my_buckets(self):
        for bucket in self.s3_client.buckets.all():
            print(bucket.name)

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
        if sys.platform == "win32":
            os.startfile(output)
        else:
            # the following works on Mac and Linux. (Darwin = mac, xdg-open = linux).
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, output])

    def list_languages(self, language):
        r_voices = self.polly_client.describe_voices(
            LanguageCode=language
        )
        for voice in r_voices['Voices']:
            print(voice)
            print(voice['Id'])

    def get_last_image(self):
        return self.m_last_image

    '''
{
   u'Labels':[
      {
         u'Confidence':98.82992553710938,
         u'Name':u'People'
      },
      {
         u'Confidence':98.82994842529297,
         u'Name':u'Person'
      },
      {
         u'Confidence':98.76869201660156,
         u'Name':u'Human'
      },
      {
         u'Confidence':83.38436126708984,
         u'Name':u'Landslide'
      }
   ],
   'ResponseMetadata':{
      'RetryAttempts':0,
      'HTTPStatusCode':200,
      'RequestId':'53c5a356-3a08-11e7-bb4d-0b9e73be3287',
      'HTTPHeaders':{
         'date':'Tue, 16 May 2017 07:21:52 GMT',
         'x-amzn-requestid':'53c5a356-3a08-11e7-bb4d-0b9e73be3287',
         'content-length':'245',
         'content-type':'application/x-amz-json-1.1',
         'connection':'keep-alive'
      }
   },
   u'OrientationCorrection':u'ROTATE_0'
}
    '''

    def what_this_image_about(self, imagePath):
        response = self.rekognize_image(self.encode_img(imagePath))
        sujet = response['Labels'][0]["Name"]
        self.tell_me("This image is about " + sujet)


rekognition_client = boto3.client('rekognition')
#print AwsWrapper().what_this_image_about('./pandaroux.jpg')
print AwsWrapper().describe_me('Montagne')
# print(AwsWrapper().tell_me("Bonjour Vincent, c'est un plaisir de vous voir."))
# Print out bucket names
