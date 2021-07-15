from .check_internet_connection import checkInternetRequests
from .download_data import statswales_get_dataset, statswales_get_metadata
from .search import statswales_search

__all__ = [
    'statswales_get_dataset',
    'statswales_get_metadata',
    'statswales_search'
]

__version__ = "0.1.0"
