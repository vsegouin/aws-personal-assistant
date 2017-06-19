import boto3


class S3Utils:
    def __init__(self):
        self.s3_client = boto3.resource('s3')

    def list_my_buckets(self):
        for bucket in self.s3_client.buckets.all():
            print(bucket.name)
