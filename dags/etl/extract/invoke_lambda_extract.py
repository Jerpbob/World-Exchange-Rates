import os

import boto3
from dotenv import load_dotenv

load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')


def create_client(
    service: str, access_key_id: str, access_secret_key: str, region_name: str
) -> boto3.client:
    client = boto3.client(
        service,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=access_secret_key,
        region_name=region_name,
    )
    return client


class InvokeLambdaFunctionExtract:

    def __init__(self, access_key_id, access_secret_key, region_name):
        self.access_key_id = access_key_id
        self.access_secret_key = access_secret_key
        self.region_name = region_name
        self.sts_client = create_client(
            'sts', self.access_key_id, self.access_secret_key, self.region_name
        )

    def assume_execution_role(self):
        response = self.sts_client.assume_role(
            RoleArn='arn:aws:iam::981217226367:role/S3Admin',
            RoleSessionName='invoke-lambda',
        )
        return response

    def invoke_lambda_function(self) -> dict:
        response = self.assume_execution_role()
        lmbda = boto3.Session(
            aws_access_key_id=response['Credentials']['AccessKeyId'],
            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
            aws_session_token=response['Credentials']['SessionToken'],
        )
        client = lmbda.client('lambda', self.region_name)
        lambda_response = client.invoke(FunctionName='upload_exchange_rates')
        return lambda_response


if __name__ == '__main__':
    test_invoke = InvokeLambdaFunctionExtract(
        ACCESS_KEY, SECRET_ACCESS_KEY, REGION_NAME
    )
    response = test_invoke.invoke_lambda_function()
    print(response)
