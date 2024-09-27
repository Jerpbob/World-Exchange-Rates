from dotenv import load_dotenv
import json
import os
import requests

def extract_api_key() -> str:
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    return API_KEY

def extract_json(currency_code: str) -> dict:
    API_KEY = extract_api_key()
    url = f'https://v6.exchangerate-api.com/v6/latest/{currency_code}'
    headers = {'Authorization': f'Bearer {API_KEY}'}

    response = requests.get(url, headers=headers)
    json_response = response.json()

    return json_response

if __name__ == '__main__':
    pass