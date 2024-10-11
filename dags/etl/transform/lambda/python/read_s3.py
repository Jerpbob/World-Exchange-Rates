import os

import duckdb
import polars as pl
from dotenv import load_dotenv
from list_s3_objects import read_s3_bucket_extracted_list

load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')


def conn_duckdb(object_name):
    bucket_name = 'exchange-rates-bucket1431'
    top10_sql = '''
            WITH top10 AS (
                SELECT 
                    base_code,
                    RANK() OVER (PARTITION BY date ORDER BY USD DESC) rnk,
                    date
                FROM rates
            )
            SELECT
                base_code,
                rnk,
                date,
            FROM top10 
            WHERE rnk <= 10
            '''

    change_overtime_sql = '''
        WITH change AS (
            SELECT
                base_code,
                USD,
                LAG(USD) OVER (PARTITION BY base_code ORDER BY date) prev_rate,
                date
            FROM rates
        ), rate_change AS (
            SELECT
                base_code,
                USD,
                USD - prev_rate change,
                date
            FROM change
            WHERE USD - prev_rate IS NOT NULL
        )
        SELECT
            base_code,
            ANY_VALUE(USD) usd_exchange_rate,
            AVG(change),
            MAX(date) date,
        FROM rate_change
        GROUP BY base_code
        HAVING AVG(change) >= 0
    '''

    con = duckdb.connect()
    con.execute('INSTALL httpfs')
    con.execute('LOAD httpfs')
    con.execute(f"SET s3_region='{REGION_NAME}'")
    con.execute(f"SET s3_access_key_id='{ACCESS_KEY}'")
    con.execute(f"SET s3_secret_access_key='{SECRET_ACCESS_KEY}'")
    con.sql(
        f"CREATE TABLE rates AS SELECT DISTINCT * FROM read_parquet('s3://{bucket_name}/{object_name}')"
    )
    con.sql(change_overtime_sql).show()


def create_table():
    pass


def filter_table():
    pass


if __name__ == '__main__':
    object_name = 'extracted/*.parquet'
    print(object_name)
    conn_duckdb(object_name)
