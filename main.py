# Dev_@ladinh production
# a currency conveter app

import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    try:
        url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey = {api_key}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'][target_currency]
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the exchange rate: {e}")
        
        return None

def convert_currency(api_key, amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    api_key = '' #API KEY pending to be inserted here...?

    amount = float(input("\nEnter the amount: "))
    base_currency = int(input("Enter the source currency code: "))
    target_currency = int(input("Enter the target currency code: "))
    
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    
    if exchange_rate is not None:
        result = convert_currency(amount, exchange_rate)
    print(f"{amount} {base_currency} is equal to {result:.2f} {target_currency}\n")
    
if __name__=="__main__":
    main()
