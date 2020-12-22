import unittest
import pandas as pd
from sw_get_dataset import sw_get_dataset

class MyTestCase(unittest.TestCase):
    def test_returns_dataframe_obj(self):
        self.assertIsInstance(sw_get_dataset("schs0235"), pd.DataFrame, "Failed")

    def test_invalid_id_returns_null(self):
        self.assertEqual(sw_get_dataset("XXXX"), None, "Failed")

    def test_numeric_input_error(self):
        self.assertEqual(sw_get_dataset(1234), None, "Failed")

    def test_list_input_error(self):
        self.assertEqual(sw_get_dataset(["schs0235", "schs0236"]), None, "Failed")

if __name__ == '__main__':
    unittest.main()