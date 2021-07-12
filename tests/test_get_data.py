import unittest
import pandas as pd
import requests
from statswales_get_dataset import statswales_get_dataset
from check_internet_connection import checkInternetRequests

class MyTestCase(unittest.TestCase):
    def test_returns_dataframe_obj(self):
        self.assertIsInstance(statswales_get_dataset("schs0235"), pd.DataFrame, "Failed")

    def test_invalid_id_returns_null(self):
        self.assertEqual(statswales_get_dataset("XXXX"), None, "Failed")

    def test_numeric_input_error(self):
        self.assertEqual(statswales_get_dataset(1234), None, "Failed")

    def test_list_input_error(self):
        self.assertEqual(statswales_get_dataset(["schs0235", "schs0236"]), None, "Failed")

if __name__ == '__main__':
    unittest.main()
