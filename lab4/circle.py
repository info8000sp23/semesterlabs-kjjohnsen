from dataclasses import dataclass
from point import Point
import math
@dataclass
class Circle:
    center: Point
    radius: float
    
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def insideSquare(self):
        from rectangle import Rectangle
        s = 2*self.radius/math.sqrt(2)
        return Rectangle(Point(self.center.x, self.center.y),s,s)
    def __str__(self):
        return(f"({self.center},r={self.radius})")
    
if __name__ == "__main__":
    c = Circle(Point(3,4),5)
    print(c)
    print(c.area())
    print(c.perimeter())
    print(c.insideSquare())