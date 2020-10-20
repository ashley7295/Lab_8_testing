import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitcoin(TestCase):

#1 get_response() gets the .json data from the API url

#2 get_bitcoin_amount() gets the user input 
    @patch('builtins.input', side_effect = [5])
    def test_get_bitcoing_amount(self, mock_input):
        amount = bitcoin.get_bitcoin_amount()
        self.assertEqual(5, amount)
#3 get_dollars_exchange() gets the specific exchange rate from teh .json data

#4 calculate_bitcoin_amount() preforms math calculation
    def test_calculate_bitcoin_amount(self):
        first_num = 1
        second_num = 2
        total = bitcoin.calculate_bitcoin_amount(first_num, second_num)
        expected_total = 2
        self.assertEqual(total, expected_total)

#5 print_exchange_rate() returns print
    @patch('builtins.print')
    def test_print_exchange_rate(self, mock_print):
        bitcoin.print_exchange_rate(5, 10)
        mock_print.assert_called_once_with('5 Bitcoin is equivilent to $10')

if __name__ == '__main__':
    unittest.main()



