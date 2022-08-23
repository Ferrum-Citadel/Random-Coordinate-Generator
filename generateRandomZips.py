"""
Getting a random point inside a country based on its name.
In this solution, the shapefile with countries was used.
"""

# imports
from os.path import exists
import sys
import json
import re
import random
import shapefile
from shapely.geometry import shape, Point

# function that takes a shapefile location and a country name as inputs
def random_point_in_country(shp_location, country_name, number_of_coordinates):
    assert exists(shp_location)
    shapes = shapefile.Reader(shp_location) # reading shapefile with pyshp library
    country = [s for s in shapes.records() if country_name in s][0] # getting feature(s) that match the country name 
    country_id = int(re.findall(r'\d+', str(country))[0]) # getting feature(s)'s id of that match

    shapeRecs = shapes.shapeRecords()
    feature = shapeRecs[country_id].shape.__geo_interface__

    shp_geom = shape(feature)

    minx, miny, maxx, maxy = shp_geom.bounds
    result = []
    i=0
    while i<number_of_coordinates:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))

        if shp_geom.contains(p):
            i+=1
            coordinates_dict = {'lat': p.y, 'lon': p.x}
            result += [coordinates_dict]
    # Write as json to file
    with open("coordinates.json", "w") as f:
        json.dump(result, f)
        

try: 
    country_name = sys.argv[1]
    number_of_coordinates = int(sys.argv[2])
    random_point_in_country("World_Countries/World_Countries.shp", country_name, number_of_coordinates)
except IndexError:
    print("Please provide the name of the country and the desired number of coordinates as an argument")