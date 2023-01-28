from math import*
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getPerimeter(self):
        return self.a + self.b + self.c
    
    def getArea(self):
        k = self.getPerimeter()
        area = sqrt(k/2*(k/2 - self.a)*(k/2 - self.b)*(k/2 - self.c))
        return area

obj = Triangle(3,4,5)
print(obj.getPerimeter())
print(obj.getArea())