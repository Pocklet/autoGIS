# Import `shapely.geometry.Point` class
from shapely.geometry import Point

# Create `Point` objects:
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point4_3D = Point(9.26, -2.456, 0.57)

print(point1)
point1


# Get coordinate tuple(s)
list(point1.coords)

# Read x and y coordinates separately
x = point1.x
y = point1.y

print(x, y)


# Calculate the distance between point1 and point2
dist = point1.distance(point2)

# Print out a nicely formatted info message
print(f"Distance between the points is {dist:.2f} units")



# import the LineString class
from shapely.geometry import LineString

# Create a LineString from our Point objects
line = LineString([point1, point2, point3])

# Create a LineString from a list of coordinates:
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
print(line== line2)
print(line)
line


# Get coordinate tuples
list(line.coords)

# Obtain x and y coordinates
xcoords = list(line.xy[0])
ycoords = list(line.xy[1])

print(xcoords)
print(ycoords)

# Get the length of the line
line_length = line.length
print(f"Length of our line: {line_length:.1f} units")

# Get the centre point of the line
print(line.centroid)



from shapely.geometry import Polygon

# Create a Polygon from the coordinates
polygon1 = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

polygon2 = Polygon([point1, point2, point3])


from shapely.geometry import LinearRing

shell = LinearRing([point1, point2, point3, point1])
polygon3 = Polygon(shell)


print(polygon1)
polygon1


# define the exterior
outer = LinearRing([(-180, 90), (-180, -90), (180, -90), (180, 90)])

# define a hole:
hole = LinearRing([(-170, 80), (-100, -80), (100, -80), (170, 80)])

outer
hole

polygon_without_hole = Polygon(outer)
polygon_without_hole

polygon_with_hole = Polygon(outer, [hole])
polygon_with_hole

print(polygon_without_hole)
print(polygon_with_hole)

print(f"Polygon centroid: {polygon_with_hole.centroid}")
print(f"Polygon area: {polygon_with_hole.area}")
print(f"Polygon bounding box: {polygon_with_hole.bounds}")
print(f"Polygon exterior ring: {polygon_with_hole.exterior}")
print(f"Polygon circumference: {polygon_with_hole.exterior.length}")


pentagon = Polygon([(30, 2.01), (31.91, 0.62), (31.18, -1.63), (28.82, -1.63), (28.09, 0.62)])
pentagon
triangle = Polygon([(0,0), (2,4), (4,0)])
triangle
square = Polygon([(0,0), (0,4), (4,4), (4,0)])
square
circle = Point((0,0))
circle.buffer(1)



from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon

# Create a MultiPoint object of our points 1,2 and 3
multipoint = MultiPoint([point1, point2, point3])

# We can also create a MultiLineString with two lines
line1 = LineString([point1, point2])
line2 = LineString([point2, point3])
multiline = MultiLineString([line1, line2])

print(multipoint)
print(multiline)
multipoint
multiline


# Let’s create the exterior of the western part of the world
western_hemisphere = Polygon([(-180, 90), (-180, -90), (0, -90), (0, 90)])
print(western_hemisphere)
western_hemisphere

from shapely.geometry import box
min_x = 0
max_x = 180
min_y = -90
max_y = 90

eastern_hemisphere = box(min_x, min_y, max_x, max_y)

print(eastern_hemisphere)
eastern_hemisphere

# Let’s create our MultiPolygon.
# Pass multiple Polygon objects as a list
multipolygon = MultiPolygon([western_hemisphere, eastern_hemisphere])

print(multipolygon)
multipolygon


# Check input geometry
multipoint

# Convex Hull
[multipoint.convex_hull, multipoint]

# Envelope (smalles rectangular polygon around a geometry/set of geometries):
multipoint.envelope
