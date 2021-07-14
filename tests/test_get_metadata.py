import unittest
import pandas as pd
import requests
from statswalespy.download_data import statswales_get_metadata

class MyTestCase(unittest.TestCase):
    def test_returns_dataframe_obj(self):
        self.assertTrue(isinstance(statswales_get_metadata("schs0235"), pd.DataFrame) or statswales_get_metadata("schs0235") is None, "Failed")

    def test_invalid_id_returns_null(self):
        self.assertEqual(statswales_get_metadata("XXXX"), None, "Failed")

    def test_numeric_input_error(self):
        self.assertEqual(statswales_get_metadata(1234), None, "Failed")

    def test_list_input_error(self):
        self.assertEqual(statswales_get_metadata(["schs0235", "schs0236"]), None, "Failed")

if __name__ == '__main__':
    unittest.main()
