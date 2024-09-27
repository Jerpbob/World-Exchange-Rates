from dotenv import load_dotenv
import json
import os
import requests

def extract_api_key() -> str:
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    return API_KEY

class Extract_API_Json():

    def __init__(self) -> None:
        self.API_KEY = extract_api_key()

    def extract_rates_json(self, currency_code: str) -> dict[str:float]:
        API_KEY = self.API_KEY
        url = f'https://v6.exchangerate-api.com/v6/latest/{currency_code}'
        headers = {'Authorization': f'Bearer {API_KEY}'}

        response = requests.get(url, headers=headers)
        json_response = response.json()

        return json_response

    def extract_codes(self) -> list[list[str]]:
        API_KEY = self.API_KEY
        url = f'https://v6.exchangerate-api.com/v6/codes'
        headers = {'Authorization': f'Bearer {API_KEY}'}

        response = requests.get(url, headers=headers)
        json_response = response.json()
        codes = json_response['supported_codes']

        return codes
    
    def convert_code_to_dict(self) -> dict[str:str]:
        codes_list = self.extract_codes()
        codes_dict = {code[0]:code[1] for code in codes_list}

        return codes_dict
    

if __name__ == '__main__':
    test = Extract_API_Json()
    print(test.convert_code_to_dict())