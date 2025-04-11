"""This lambda function copy objects from one bucket to other"""
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    source_key = event["Records"][0]["s3"]["object"]["key"]

    object_copy = s3_client.copy_object(
        Bucket="copy-bucket-psg",
        CopySource = {'Bucket': source_bucket, 'Key': source_key},
        Key = source_key
    )

    print("Object is copied")
