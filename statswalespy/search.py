"""
Function for searching StatsWales tables using key strings.
"""
import requests
import pandas as pd
import logging
from statswalespy.check_internet_connection import checkInternetRequests

def statswales_search(search_text):

    # If intput is a list of strings, check they are strings
    if type(search_text) == list:
        for item in search_text:
            if type(item) != str:
                logging.warning("Please enter search term as a string or list of strings.")
                return None
            else:
                pass

    # If item is not a list, check that it's a strings
    if type(search_text) != list and type(search_text) != str:
        logging.warning("Please enter search term as a string or list of strings.")
        return None
    else:
        pass

    # Check for internet connection and return none with an error message if there is no connection
    if checkInternetRequests():
        pass
    else:
        logging.warning("Internet connection not found.")
        return None

    url = "http://open.statswales.gov.wales/en-gb/discover/metadata?$filter=Tag_ENG%20eq%20%27Title%27"

    request = requests.get(url)

    if request.status_code == 200:
        pass
    else:
        return None

    json_data = request.json()['value']

    dataframe = pd.DataFrame(json_data)

    dataframe = dataframe[["Dataset", "Description_ENG"]]


    if type(search_text) == list:
        search_text = "|".join(search_text)

    dataframe = dataframe[dataframe.Description_ENG.str.contains(search_text, regex = True, case = False)]

    return dataframe
