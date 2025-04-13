"""This lambda function copy objects from one bucket to other"""
import boto3
import os
import logging
from http import HTTPStatus

s3_client = boto3.client('s3')
destination_bucket = os.getenv("destination_bucket")

logging.getLogger().setLevel("INFO")

def lambda_handler(event, context):
    source_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    source_key = event["Records"][0]["s3"]["object"]["key"]

    try:
        object_copy = s3_client.copy_object(
            Bucket = destination_bucket,
            CopySource = {'Bucket': source_bucket, 'Key': source_key},
            Key = source_key
        )
    except s3_client.exceptions.NoSuchBucket as err:
        logging.error("Destination or source bucket not present")
        raise Exception(f"Error: {err}")

    if object_copy["ResponseMetadata"]["HTTPStatusCode"] != HTTPStatus.OK:
        raise Exception(f"Object {source_key} failed to get copied")

    logging.info("Object is copied")
