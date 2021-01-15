import unittest
import pandas as pd
import requests
from statswales_search import statswales_search
from check_internet_connection import checkInternetRequests

class MyTestCase(unittest.TestCase):
    def test_returns_dataframe(self):
        self.assertIsInstance(statswales_search("schools"), pd.DataFrame, "Failed")

    def test_noncharacter_null(self):
        self.assertEqual(statswales_search(1234), None, "Failed")

if __name__ == '__main__':
    unittest.main()
