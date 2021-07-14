
import requests
import pandas as pd
import logging
from statswalespy.check_internet_connection import checkInternetRequests

"""
Function for extracting StatsWales datasets.
"""

def statswales_get_dataset(id, print_progress=False):

    # Check the user has inputted a single value
    if(isinstance(id, list)):
        print("Please enter one id value.")
        return None


    # Check id input is a string
    if (type(id) is not str):
        print("Please enter id as a string")
        return None

    # Check for internet connection and return none with an error message if there is no connection
    if checkInternetRequests():
        pass
    else:
        logging.warning("Internet connection not found.")
        return None

    # Define dataset URL --------------------------------------------------------
    url = "http://open.statswales.gov.wales/en-gb/dataset/" + id

    # Check if the resource is unavailable
    try:
        first_request = requests.get(url, timeout = 10)
    except requests.exceptions.Timeout:
        logging.warning("The StatsWales API did not respond in time and might be unavailable.")
        return None

    # Exit if the object returned has status code 404
    if first_request.status_code == 404:
        logging.warning("Dataset was not found. Check your dataset id for typos. If your dataset id is correct, the API might be unavailable.")
        return None

    # Extract first page and add dataframe to list ------------------------------
    json_data = first_request.json()

    # Add this set of json_data to a list
    json_list = [json_data['value']]

    # Loop through odata links to get all data --------------------------------
    i = 0

    no_response = False

    while "odata.nextLink" in json_data:

        # print progress message
        if print_progress:
            i = i + len(json_data['value'])
            print("Extracting data: " + str(i) + " rows extracted")

        try:
            json_data = requests.get(json_data["odata.nextLink"], timeout = 10).json()

            json_list.append(json_data['value'])
        except requests.exceptions.Timeout:
            logging.warning("The StatsWales API did not respond in time and might be unavailable.")
            no_response = True
            break # While look is broken if the API does not respond

    # Exit function if any of the pages do not respond in time - covers the
    # rare occasion when the API goes down mid-call
    if no_response:
        return None


    # bind dataframes together and tell user the data is extracted
    json_flat = [l for json in json_list for l in json]
    df = pd.DataFrame(json_flat)

    print("Data extracted with " + str(len(df)) + " rows, and " + str(len(df.columns)) + " columns.")

    # Return the dataframe
    return df

"""
Function for extracting StatsWales metadata.
"""

def statswales_get_metadata(id) :

    # Check the user has inputted a single value
    if(isinstance(id, list)):
        print("Please enter one id value.")
        return None


    # Check id input is a string
    if (type(id) is not str):
        print("Please enter id as a string")
        return None

    # Check internet connection
    if checkInternetRequests():
        pass
    else:
        logging.warning("Internet connection not found.")
        return None

    # Define StatsWales URL
    url = "http://open.statswales.gov.wales/en-gb/discover/metadata?$filter=Dataset%20eq%20%27" + id.lower() + "%27"

    # Check if the resource is unavailable
    try:
        request = requests.get(url, timeout = 10)
    except requests.exceptions.Timeout:
        logging.warning("The StatsWales API did not respond in time and might be unavailable.")
        return None

    if request.status_code == 404:
        logging.warning("Metadata was not found. Check your dataset id for typos. If your dataset id is correct, the API might be unavailable.")
        return None

    json_data = request.json()

    metadata = pd.DataFrame(json_data['value'])

    if metadata.empty:
        logging.warning("Metadata was not found. Check your dataset id for typos. If your dataset id is correct, the API might be unavailable.")
        return None


    return metadata
