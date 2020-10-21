import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitcoin(TestCase):
    test_response = {
        "time": {
            "updated": "Oct 20, 2020 15:03:00 UTC",
            "updatedISO": "2020-10-20T15:03:00+00:00",
            "updateduk": "Oct 20, 2020 at 16:03 BST"
        },
        "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName": "Bitcoin",
        "bpi": {
            "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "11,906.8495",
            "description": "United States Dollar",
            "rate_float": 11906.8495
            },
            "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "9,180.5382",
            "description": "British Pound Sterling",
            "rate_float": 9180.5382
            },
            "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "10,073.3614",
            "description": "Euro",
            "rate_float": 10073.3614
            }
        }
    }


    @patch('bitcoin.get_exchange_rate_data', side_effect=[test_response])
    def test_get_exchange_rate_data(self, mock_response):
        response = bitcoin.get_exchange_rate_data()
        self.assertEqual(response, self.test_response)


    #get_bitcoin_amount() gets the user input 
    @patch('builtins.input', side_effect = [5])
    def test_get_bitcoing_amount(self, mock_input):
        amount = bitcoin.get_bitcoin_amount()
        self.assertEqual(5, amount)

    #calculate_bitcoin_amount() preforms math calculation
    def test_calculate_bitcoin_amount(self):
        first_num = 1
        second_num = 2
        total = bitcoin.calculate_bitcoin_amount(first_num, second_num)
        expected_total = 2
        self.assertEqual(total, expected_total)

    #print_exchange_rate() returns print
    @patch('builtins.print')
    def test_print_exchange_rate(self, mock_print):
        bitcoin.print_exchange_rate(5, 10)
        mock_print.assert_called_once_with('5 Bitcoin is equivilent to $10')



if __name__ == '__main__':
    unittest.main()



