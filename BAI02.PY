import re

from shapely.geometry import Point, Polygon

with open("BAI02.INP", "r") as file:
    content = file.read()

points_str = re.sub("\s+", " ", content)
points = list(
    map(lambda x: tuple([int(c) for c in x.split(",")]), points_str.split(" "))
)
polygon_points = points[:-1]
point = points[-1]


def is_valid_polygon(points):
    # Ensure at least 3 points to form a polygon
    if len(points) < 3:
        return False, None
    # Create a Shapely Polygon object
    polygon = Polygon(points)
    # Check if the polygon is valid (closed and non-self-intersecting)
    return polygon.is_valid, polygon


def is_point_inside_polygon(point, polygon_points):
    is_valid, polygon = is_valid_polygon(polygon_points)
    if not is_valid:
        return 0, 0
    point = Point(point)

    return int(is_valid), int(point.within(polygon))


with open("BAIO2.OUT", "w") as file:
    for line in is_point_inside_polygon(point, polygon_points):
        file.write(str(line) + "\n")
