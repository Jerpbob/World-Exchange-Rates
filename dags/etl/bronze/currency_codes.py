def top_25_exchange_rates() -> dict[str, str]:
    # https://www.countries-ofthe-world.com/most-traded-currencies.html
    return {
        'USD': 'United States Dollar',
        'EUR': 'European Euro',
        'JPY': 'Japanese Yen',
        'GBP': 'Pound Sterling',
        'AUD': 'Australian Dollar',
        'CAD': 'Canadian Dollar',
        'CHF': 'Swiss Franc',
        'CNY': 'Chinese Yuan Renminbi',
        'SEK': 'Swedish Krona',
        'MXN': 'Mexican Peso',
        'NZD': 'New Zealand Dollar',
        'SGD': 'Singapore Dollar',
        'HKD': 'Hong Kong Dollar',
        'NOK': 'Norwegian Krone',
        'KRW': 'South Korean Won',
        'TRY': 'Turkish Lira',
        'INR': 'Indian Rupee',
        'RUB': 'Russian Ruble',
        'BRL': 'Brazilian Real',
        'ZAR': 'South African Rand',
        'DKK': 'Danish Krone',
        'PLN': 'Polish Zloty',
        'TWD': 'New Taiwan Dollar',
        'THB': 'Thai Baht',
        'MYR': 'Malaysian Ringgit',
    }


if __name__ == '__main__':
    print(len(top_25_exchange_rates()))
