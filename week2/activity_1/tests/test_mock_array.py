import unittest
from src.mock_array import Array
from unittest.mock import patch

class TestMockArray(unittest.TestCase):
    def setUp(self):
        self.mock_array = Array(max_size=2)

    def tearDown(self):
        del self.mock_array

    def test_get_inserted_item(self):
        self.mock_array.append(1)
        self.mock_array.append(2)
        self.assertEqual(self.mock_array.get(0), 1)
        self.assertEqual(self.mock_array.get(1), 2)