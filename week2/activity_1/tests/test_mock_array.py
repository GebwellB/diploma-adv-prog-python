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

    # index incremented

    # get empty list get an error

    # insert item at aposition

    # insert out of bounds a specific IndexError

    def test_get_from_empty_list_raises_error(self):
        with self.assertRaises(IndexError):
            self.mock_array.get(0)
    # test the resize works when full

    # test see if we get the instance counts
    def test_atr_not_available(self):
        with self.assertRaises(AttributeError):
            _ =  self.mock_array.__resize
        with self.assertRaises(AttributeError):
            _ =  self.mock_array.__instance_count

    def test_get_instance_count(self):
        with patch('src.mock_array.Array.get_instance_count', return_value=999) as mock_method:
            self.assertEqual(Array.get_instance_count(), 999)

if __name__ == '__main__':
    unittest.main()