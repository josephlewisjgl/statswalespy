"""

StatsWalesPy will be a package that takes data from StatsWales into Python.
This file contains the function to search StatsWales tables using key strings.

"""

import requests
import pandas as pd

def statswales_search(search_text):
    
    if checkInternetRequests():
        pass
    else:
        print("Internet connection not found.")
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