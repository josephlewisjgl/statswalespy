"""

StatsWalesPy will be a package that takes data from StatsWales into Python.
This file contains the function to get metadata associated with a dataset using the StatsWales API.

"""
import requests
import pandas as pd
from check_internet_connection import checkInternetRequests

def statswales_get_metadata(id) :

    if checkInternetRequests():
        pass
    else:
        print("Internet connection not found.")
        return None

    url = "http://open.statswales.gov.wales/en-gb/discover/metadata?$filter=Dataset%20eq%20%27" + id.lower() + "%27"

    request = requests.get(url)

    if request.status_code == 200:
        pass
    else:
        return None

    json_data = request.json()

    metadata = json_data['value']

    return pd.DataFrame(metadata)
