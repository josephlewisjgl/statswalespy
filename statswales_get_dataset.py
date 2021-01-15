"""

StatsWalesPy will be a package that takes data from StatsWales into Python.
This file contains the function to get this data using the OData feed from a known cube.

"""
import requests
import pandas as pd
from check_internet_connection import checkInternetRequests

def statswales_get_dataset(id, print_progress=False):

    # Check id input is a string
    if (type(id) is not str):
        print("Please enter id as a string")
        return None

    # Check for internet connection and return none with an error message if there is no connection
    if checkInternetRequests():
        pass
    else:
        print("Internet connection not found.")
        return None

    # Define dataset URL --------------------------------------------------------
    url = "http://open.statswales.gov.wales/en-gb/dataset/" + id

    # Extract first page and add dataframe to list ------------------------------
    try:
        json_data = requests.get(url).json()
    except ValueError:
        print("Dataset was not found. Check your dataset id for typos. If your dataset id is correct, the API might "
              "be unavailable.")
        return None

    # Add this set of json_data to a list
    json_list = [json_data['value']]

    # Loop through odata links to get all data --------------------------------
    i = 0

    while "odata.nextLink" in json_data:

        # print progress message
        if print_progress:
            i = i + len(json_data['value'])
            print("Extracting data " + str(i) + " rows extracted")

        json_data = requests.get(json_data["odata.nextLink"]).json()

        json_list.append(json_data['value'])

    # bind dataframes together and tell user the data is extracted
    json_flat = [l for json in json_list for l in json]
    df = pd.DataFrame(json_flat)

    print("Data extracted with " + str(len(df)) + " rows, and " + str(len(df.columns)) + " columns.")

    # Return the dataframe
    return df
