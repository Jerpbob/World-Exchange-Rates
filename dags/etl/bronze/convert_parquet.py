from datetime import datetime
from pathlib import Path

import polars as pl
from currency_codes import top_25_exchange_rates
from extract_api import extract_all_rates


def create_polars_df(
    exchange_rates: list[dict[str, str | float]]
) -> pl.DataFrame:
    top_25_codes = top_25_exchange_rates().keys()
    today = datetime.today()
    date = datetime(today.year, today.month, today.day)

    df = pl.DataFrame(exchange_rates)
    filtered_df = df.select(['base_code', *top_25_codes]).with_columns(
        date=date
    )
    return filtered_df


def create_exchange_rate_parquet() -> None:

    exchange_rates = extract_all_rates()
    polars_df = create_polars_df(exchange_rates)
    polars_df.write_parquet('parquet_files/test3.parquet')


def display_parquet() -> None:
    df = pl.read_parquet(Path('parquet_files') / 'test3.parquet')
    print(df)


if __name__ == '__main__':
    # create_exchange_rate_parquet()
    # display_parquet()
    today = datetime.today()
    date = datetime(today.year, today.month, today.day)
    print(type(date), date)
