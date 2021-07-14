# statswalespy
> Easily download data and metadata from the StatsWales API

statswalespy is a Python package for interacting with the [StatsWales](https://statswales.gov.wales/Catalogue) API,
including functions for downloading datasets, downloading metadata, and searching for datasets using key words.

## How to download data and metadata

The code below extracts data about [aircraft movement at Cardiff
airport](https://statswales.gov.wales/Catalogue/Transport/Air/aircraftmovementsatcardiffairport-by-movementtype-year)
and the associated metadata.

``` python
from statswalespy.download_data import statswales_get_dataset, statswales_get_metadata

metadata = statswales_get_metadata("tran0003")

data = statswales_get_dataset("tran0003")
```

## How to search for datasets

You can also search for datasets based on key terms. For example, data on farming or agriculture can be searched using this code:

``` python
from statswalespy.search import statswales_search

farming_datasets = statswales_search(["farm*", "agri*"])
```
