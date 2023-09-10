from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon

# define function point
def create_point_geometry(x, y):
    return Point(x, y)

point1 = create_point_geometry(0.0, 1.1)
print(point1)
print(point1.geom_type)



# define function line
def create_line_geometry(list):
    assert len(list) > 2, "Minimum two points"
    assert type(list) == tuple, "Must be a list"
    return LineString(list)

list1 = ((2.2, 4.2), (7.2, -25.1), (9.26, -2.456))
print(type(list1))

line1 = create_line_geometry(list1)
print(line1)
print(line1.geom_type)



# define function polygon
def create_polygon_geometry(coord):
    assert len(coord) > 2, "Minimum two points"
    assert type(coord) == tuple, "Must be a list"
    return Polygon(coord)

list2 = ((45.2, 22.34), (100.22, -3.20), (70.0, 10.20))

polygon1 = create_polygon_geometry(list2)
print(polygon1)
print(polygon1.geom_type)



# define function centroid
def get_centroid(geom):
    return geom.centroid

centroid = get_centroid(polygon1)
print(centroid)



# define function area
def get_area(polygon):
    return polygon.area

area = get_area(polygon1)
print(round(area, 2))



# define function length
def get_length(geometry):
    if type(geometry) == LineString:
        return geometry.length
    elif type(geometry) == Polygon:
        return geometry.exterior.length
    else:
        print("Not valid type")
    

lineLength = get_length(line1)
print(lineLength)

polygonLength = get_length(polygon1)
print(polygonLength)




