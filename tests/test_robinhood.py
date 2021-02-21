import json
import os
import robinhood as rh
import unittest
import uuid

class TestFunctions(unittest.TestCase):
    def test_generate_device_token(self):
        self.assertIsInstance(uuid.UUID(rh.generate_device_token()), uuid.UUID)

class TestRobinhood(unittest.TestCase):
    def test_robinhood(self):
        with open('config.json') as f:
            config = json.load(f)

        device_token = config['device_token'] or os.environ.get('ROBINHOOD_DEVICE_TOKEN')
        username = config['username'] or os.environ.get('ROBINHOOD_USERNAME')
        password = config['password'] or os.environ.get('ROBINHOOD_PASSWORD')

        self.assertIsInstance(rh.Robinhood(device_token, username, password), rh.Robinhood)
        self.assertRaises(Exception, rh.Robinhood, device_token, username, '')
        self.assertRaises(Exception, rh.Robinhood, device_token, '', password)
        self.assertRaises(Exception, rh.Robinhood, device_token, '', '')
        self.assertRaises(Exception, rh.Robinhood, '', username, password)
        self.assertRaises(Exception, rh.Robinhood, '', username, '')
        self.assertRaises(Exception, rh.Robinhood, '', '', password)
        self.assertRaises(Exception, rh.Robinhood, '', '', '')
