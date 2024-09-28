import os

import requests
from currency_codes import top_25_exchange_rates
from dotenv import load_dotenv


def extract_api_key() -> str | None:
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    return API_KEY


def extract_rates_json(currency_code: str) -> dict[str, dict | str]:
    API_KEY = extract_api_key()
    url = f'https://v6.exchangerate-api.com/v6/latest/{currency_code}'
    headers = {'Authorization': f'Bearer {API_KEY}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print('HTTP Error')
        print(errh.args[0])
        raise
    except requests.exceptions.ConnectionError:
        print('Connection Error')
        raise

    return response


def combine_base_code_dict(
    json_rate_response: dict[str, dict | str]
) -> dict[str, str | float]:
    '''
    Makes a dictionary with exchange rates and its respective base code,
    basically it flattens the json
    '''
    base_code_dict = {'base_code': json_rate_response['base_code']}
    exchange_rates_dict = json_rate_response['conversion_rates']

    # combine the two dictionaries
    base_code_and_exchange_rates_dict = base_code_dict | exchange_rates_dict
    return base_code_and_exchange_rates_dict


def create_rates_flattened_json(currency_code: str) -> dict[str, str | float]:
    '''
    Returns dictionary of format:
    {
        base_code: USD,
        USD: 1,
        AWS: 2.2939,
        etc.
    }
    '''
    json_response = extract_rates_json(currency_code)
    test_dict = combine_base_code_dict(json_response)
    return test_dict


def extract_all_rates() -> list[dict[str, str | float]]:
    # list to hold all the dictionaries of all the supported base codes
    exchange_rates_list = []
    codes = top_25_exchange_rates()
    codes_list = codes.keys()
    for code in codes_list:
        exchange_rates_dict = create_rates_flattened_json(code)
        exchange_rates_list.append(exchange_rates_dict)
    return exchange_rates_list


if __name__ == '__main__':
    print(extract_all_rates())
