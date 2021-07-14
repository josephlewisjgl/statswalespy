# Statwalespy

statswalespy is a package for downloading datasets and their associated metadata from StatsWales. This functionality is limited to datasets that are available through the OData feed. You can check this by navigating to your desired dataset, scrolling to the bottom, and checking that the “Dataset” link is available under the Open Data tab.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install statswalespy.

```bash
pip install statswalespy
```

## Usage
Import statswalespy
```python
import statswalespy
```

Return a Pandas DataFrame with data from the StatsWales cube : 'KS4 indicators by year and SEN (Special educational need) provision'.

```python 
df = statswalespy.statswales_get_dataset('SCH0192')
print(str(df))

#             Data Measure_Code  ... Year_ItemName_ENG Year_SortOrder
#0       82.310659           L2  ...              2012              8
#1      351.578548           CP  ...              2017             13
#2    28611.000000       Cohort  ...              2010              6
#3       75.376921          SCI  ...              2011              7
#4       73.160672          ENG  ...              2010              6
#5       73.243233          ENG  ...              2012              8
```
Return all metadata associated with the same cube.
```python
metadata = statswalespy.statswales_get_metadata('SCH0192')
print(str(metadata))

#     Dataset  ...                     Timestamp
#0   schs0192  ...  2020-01-30T10:31:42.9403647Z
#1   schs0192  ...  2020-01-30T10:31:42.9403647Z
#2   schs0192  ...  2020-01-30T10:31:42.9403647Z
#3   schs0192  ...  2020-01-30T10:31:42.9403647Z
#4   schs0192  ...  2020-01-30T10:31:42.9403647Z
#5   schs0192  ...  2020-01-30T10:31:42.9403647Z
```
Return a DataFrame containing all the cube titles and references that match the keyword school.
```python
search = statswalespy.statswales_search('school')
print(str(search))

#       Dataset                                    Description_ENG
#251   schs0203               Pupils (FTE) by school and age group
#253   schs0206            Pupils (number) by school and age group
#258   schs0213         Support staff (FTE) by school and category
#261   schs0216      Support staff (number) by school and category
#264   schs0219              Teachers (FTE) by school and category
#266   schs0222           Teachers (number) by school and category

```

## Contributing
Any suggestions for changes or extra work to make the package better are welcome.

## License
add
