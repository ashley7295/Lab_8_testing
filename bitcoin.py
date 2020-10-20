import requests
from pprint import pprint


def main():
    data = get_response()

    bitcoin_amount = get_bitcoin_amount()
    exchange_rates = get_dollars_exchange_rate(data)
    bitcoin_value = calculate_bitcoin_amount(bitcoin_amount, exchange_rates)

    print_exchange_rate(bitcoin_amount, bitcoin_value)

def get_response():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(url)
    data = response.json()
    return data

def get_bitcoin_amount():
    bitcoin_amount = float(input('How many bitcoins do you have?: '))
    return bitcoin_amount


def get_dollars_exchange_rate(data):

    dollars_exchange_rate = data['bpi']['USD']['rate_float']

    return dollars_exchange_rate

def calculate_bitcoin_amount(bitcoin_amount, exchange_rate):
    bitcoin_value = bitcoin_amount * exchange_rate
    return bitcoin_value

def print_exchange_rate(bitcoin_amount, bitcoin_value):
    return print (f'{bitcoin_amount} Bitcoin is equivilent to ${bitcoin_value:,}')


if __name__ == '__main__':
    main()
