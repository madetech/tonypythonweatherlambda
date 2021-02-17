import json
import sys
import boto3
import os
import requests
ssm = boto3.client("ssm")
def get_ssm_secret(parameter):
    return ssm.get_parameter(
        Name=parameter,
        WithDecryption=True
    )
def lambda_handler(event, context):
    secret = get_ssm_secret(os.environ.get('API_SSM_PARAMETER'))
    url = os.environ.get('API_URL') + "/data/2.5/weather?q=london&appid=" + secret.get("Parameter").get("Value")
    response = requests.get(url)
    print(response)
    print("Weather in London is: ")
