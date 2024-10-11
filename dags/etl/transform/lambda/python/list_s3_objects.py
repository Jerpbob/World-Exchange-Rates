import os

import boto3
from dotenv import load_dotenv

load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')


def create_client(
    service: str, access_key_id: str, access_secret_key: str, region_name: str
) -> str:
    client = boto3.client(
        service,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=access_secret_key,
        region_name=region_name,
    )
    return client


def read_s3_bucket_extracted_list(num_objects: int) -> list[str]:
    client = create_client('s3', ACCESS_KEY, SECRET_ACCESS_KEY, REGION_NAME)
    response = client.list_objects_v2(
        Bucket='exchange-rates-bucket1431',
        Prefix='extracted/',
        MaxKeys=num_objects,
    )
    content = response['Contents']
    return [x['Key'] for x in content]


if __name__ == '__main__':
    s3_list = read_s3_bucket_extracted_list(3)
    print(s3_list)
