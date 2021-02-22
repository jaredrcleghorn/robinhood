import json
import os
import re
import robinhood as rh
import unittest
import uuid

class TestFunctions(unittest.TestCase):
    def test_generate_device_token(self):
        self.assertIsInstance(uuid.UUID(rh.generate_device_token()), uuid.UUID)

class TestRobinhood(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRobinhood, self).__init__(*args, **kwargs)

        with open('config.json') as f:
            config = json.load(f)

        self.device_token = config['device_token'] or os.environ.get('ROBINHOOD_DEVICE_TOKEN')
        self.username = config['username'] or os.environ.get('ROBINHOOD_USERNAME')
        self.password = config['password'] or os.environ.get('ROBINHOOD_PASSWORD')

    def setUp(self):
        self.robinhood = rh.Robinhood(self.device_token, self.username, self.password)

    def test_robinhood(self):
        self.assertIsInstance(self.robinhood, rh.Robinhood)
        self.assertRaises(Exception, rh.Robinhood, self.device_token, self.username, '')
        self.assertRaises(Exception, rh.Robinhood, self.device_token, '', self.password)
        self.assertRaises(Exception, rh.Robinhood, self.device_token, '', '')
        self.assertRaises(Exception, rh.Robinhood, '', self.username, self.password)
        self.assertRaises(Exception, rh.Robinhood, '', self.username, '')
        self.assertRaises(Exception, rh.Robinhood, '', '', self.password)
        self.assertRaises(Exception, rh.Robinhood, '', '', '')

    def test_get_positions(self):
        positions = self.robinhood.get_positions()

        self.assertIs(type(positions), tuple)

        for position in positions:
            symbol = position['symbol']

            self.assertIs(type(symbol), str)
            self.assertTrue(re.search('^[A-Z]+$', symbol))

            quantity = position['quantity']

            self.assertIs(type(quantity), float)
            self.assertTrue(quantity > 0)

    def test_get_historicals(self):
        historicals = self.robinhood.get_historicals('TSLA')

        self.assertIs(type(historicals), tuple)

        for historical in historicals:
            begins_at = historical['begins_at']

            self.assertIs(type(begins_at), str)
            self.assertTrue(re.search('^[0-9]{4}(-[0-9]{2}){2}$', begins_at))

            close_price = historical['close_price']

            self.assertIs(type(close_price), float)
            self.assertTrue(close_price > 0)
