from circle import Circle
from point import Point
from rectangle import Rectangle
def point_rectangle(p: Point, r: Rectangle):
    temp = p - r.center #finds p relative to the center of rectangle
    return abs(temp.x) < r.width and abs(temp.y) < r.height

def point_circle(p: Point, c: Circle):
    return (p-c.center).length() < c.radius

def rectangle_rectangle(r1: Rectangle, r2: Rectangle):
    between: Point = r2.center - r1.center # vector between them
    if abs(between.x) > r1.width/2 + r2.width/2: return False
    if abs(between.y) > r1.height/2 + r2.height/2: return False
    return True

def circle_circle(c1: Circle, c2: Circle):
    between: Point = c1.center - c2.center
    return between.length() < (c1.radius + c2.radius)

def rectangle_circle(r: Rectangle, c: Circle):
    clamp_x = clamp(r.center.x-r.width/2,r.center.x+r.width/2,c.center.x)
    clamp_y = clamp(r.center.y-r.height/2,r.center.y+r.height/2,c.center.y)
    return point_circle(Point(clamp_x,clamp_y),c)

def clamp(lower: float,upper: float, value: float):
    return max(lower, min(upper, value))

if __name__=="__main__":
    print(clamp(3,7,10))
    print(rectangle_circle(Rectangle(Point(3,4),3,7),Circle(Point(3,9),2)))