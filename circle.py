from math import pi
class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def getArea(self):
        """
        This method finds the area of the Circle.

        Args:
            No
        Returns:
            float or int: result.
        """
        return pi*self.r**2

    def getLength(self):
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        return 2*pi*self.r
circle = Circle(r=5)
print(circle.getArea())
print(circle.getLength())