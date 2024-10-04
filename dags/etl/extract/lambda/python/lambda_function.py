import boto3
from convert_parquet import create_exchange_rate_parquet
import json

s3_client = boto3.client('s3')
S3_BUCKET = 'exchange-rates-bucket1431'
LOCAL_FILE_SYS = '/tmp/'

def upload_parquet_to_s3() -> None:
    filename = create_exchange_rate_parquet()
    s3_client.upload_file(
        LOCAL_FILE_SYS + filename,
        S3_BUCKET,
        'extracted/' + filename
    )

def lambda_handler(event, context):
    upload_parquet_to_s3()
    return {
        'statusCode': 200,
        'body': json.dumps('Extraction worked!')
    }