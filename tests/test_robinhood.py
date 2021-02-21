import robinhood as rh
import unittest
import uuid

class TestFunctions(unittest.TestCase):
    def test_generate_device_token(self):
        self.assertIsInstance(uuid.UUID(rh.generate_device_token()), uuid.UUID)
