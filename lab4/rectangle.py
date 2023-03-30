from dataclasses import dataclass
from point import Point

@dataclass
class Rectangle:
    center: Point
    width: float
    height: float

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return self.width*2 + self.height*2
    def getPoints(self):
        return [
            self.center + Point(-self.width/2, -self.height/2), #LL
            self.center + Point(self.width/2,-self.height/2), #LR
            self.center + Point(-self.width/2, self.height/2), #UL
            self.center + Point(self.width/2, self.height/2), #UR
        ]
    def boundingCircle(self):
        from circle import Circle
        return Circle(self.center, Point(self.width/2,self.height/2).length())
    def __str__(self):
        return f"|{self.center},w={self.width},h={self.height}|"
    
if __name__=="__main__":
    R = Rectangle(Point(0,0),6,8)
    print(R)
    print(R.getPoints())
    print(R.area())
    print(R.perimeter())
    print(R.boundingCircle())