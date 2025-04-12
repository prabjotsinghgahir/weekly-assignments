"""This lambda function copy objects from one bucket to other"""
import boto3
import os
from http import HTTPStatus

s3_client = boto3.client('s3')
destination_bucket = os.getenv("destination_bucket")

def lambda_handler(event, context):
    source_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    source_key = event["Records"][0]["s3"]["object"]["key"]

    object_copy = s3_client.copy_object(
        Bucket=destination_bucket,
        CopySource = {'Bucket': source_bucket, 'Key': source_key},
        Key = source_key
    )
    if object_copy["ResponseMetadata"]["HTTPStatusCode"] != HTTPStatus.OK:
        raise Exception(f"Object {source_key} failed to get copied")
    print("Object is copied")
