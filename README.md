# Statwalespy

statswalespy is a package for downloading datasets and their associated metadata from StatsWales. This functionality is limited to datasets that are available through the OData feed. You can check this by navigating to your desired dataset, scrolling to the bottom, and checking that the “Dataset” link is available under the Open Data tab.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install statswalespy.

```bash
pip install statswalespy
```

## Usage

```python
import statswalespy

# returns a Pandas DataFrame with data from the StatsWales cube :
#'KS4 indicators by year and SEN (Special educational need) provision'
df = statswalespy.statswales_get_dataset('SCH0192')
print(df)

# add results

# returns all metadata associated with the same cube
statswalespy.statswales_get_metadata('SCH0192')

# add results 

# returns a DataFrame containing all the cube titles and references that match the keyword school
statswalespy.statswales_search('school*')

# add results 

```

## Contributing
Any suggestions for changes or workings to make the package better are welcome.

## License
# add
