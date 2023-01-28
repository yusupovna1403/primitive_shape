from math import fabs
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_from_Xcoordinate(self):
        """
        This method finds the distance between a point and its X coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return fabs(self.y)

    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return fabs(self.x)

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            if self.x == 0 and self.y != 0:
                return "The point on the y coordinate"
            if self.x != 0 and self.y == 0:
                return "The point on the x coordinate" 
        
        

    def on_Xcoordinate(self):
        """
        This method checks for a point on the X coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        if self.x != 0 and self.y == 0:
            return True
        else:
            return False
        

    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        if self.x == 0 and self.y != 0:
            return True
        else:
            return False

point = Point(x=0,y=-6)
point1 = Point(x=-3,y=4)
print(point.distance_from_Xcoordinate())
print(point.distance_from_Ycoordinate())
print(point.getQuadrant())
print(point.on_Xcoordinate())
print(point.on_Ycoordinate())
print(point1.getQuadrant())

 