import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def distance(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)
    
def main():
    point = Point(3, 4)
    print("X: ", point.x)
    print("Y: ", point.y)
    print("Distance: ", point.distance)

if __name__ == "__main__":
    main()