from dataclasses import dataclass
import math
@dataclass
class Point:
    x: float
    y: float

    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
    
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    
    def __str__(self):
        return f"<{self.x},{self.y}>"
    
if __name__=="__main__":
    print(Point(3,4))
    print(Point(2,3)+Point(3,4))
    print(Point(2,3)-Point(3,5))
    print(Point(3,4).length())