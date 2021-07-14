import unittest
import pandas as pd
import requests
from statswalespy.search import statswales_search

class MyTestCase(unittest.TestCase):
    def test_returns_dataframe(self):
        self.assertTrue(isinstance(statswales_search("schools"), pd.DataFrame) or statswales_search("schools") is None, "Failed")

    def test_noncharacter_null(self):
        self.assertEqual(statswales_search(1234), None, "Failed")

if __name__ == '__main__':
    unittest.main()
