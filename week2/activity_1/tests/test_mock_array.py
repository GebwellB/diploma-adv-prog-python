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

    def test_private_attributes_not_accessible(self):
        with self.assertRaises(AttributeError):
            _ = self.mock_array.__resize
        with self.assertRaises(AttributeError):
            _ = self.mock_array.__instance_count

    def test_class_method_get_instance_count(self):
        # This assumes the test suite is run independently
        self.assertGreaterEqual(Array.get_instance_count(), 1)

    def test_mock_instance_count_method(self):
        with patch('src.mock_array.Array.get_instance_count', return_value=999) as mock_method:
            self.assertEqual(Array.get_instance_count(), 999)
            mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()