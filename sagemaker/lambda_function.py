import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    #data = json.dumps(event)

    payload = event["queryStringParameters"]["data"]
    print('this is what data looks like ', payload )
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    result = json.loads(response['Body'].read().decode())

    predicted_label = result
    # try "body": {"crimeCategory": json.dumps(predicted_label)}
    return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(predicted_label)
            }
