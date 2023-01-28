from polygon import Polygon

class Square(Polygon):
    def __init__(self, height) -> None:
        super().__init__(height,height)

x = Square(6)
print(x.getArea())
print(x.getPerimeter())
    