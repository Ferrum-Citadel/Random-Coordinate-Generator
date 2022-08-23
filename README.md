# Random-Coordinate-Generator

**Generate a number of random coordinates contained within a country of your choice and export to JSON file**. 
- Example of exported coordinates format:

```
[
  {"lat": 36.32624626720135, "lon": 28.05612425821899},
  {"lat": 40.43752023176555, "lon": 23.33709578949079}
]
```
- Example Usage:
```
python3 generateRandomZips.py Greece 1000 
```

Code for parsing the shapefile taken from: https://gis.stackexchange.com/a/368151

