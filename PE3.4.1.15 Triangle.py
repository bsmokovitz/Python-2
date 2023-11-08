import math
class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertices = [vertice1, vertice2, vertice3]
    def perimeter(self):
        perimeter = 0
        for i in range(3):
            perimeter += math.sqrt((self.vertices[i].x - self.vertices[(i + 1) % 3].x) ** 2 + (self.vertices[i].y - self.vertices[(i + 1) % 3].y) ** 2)
        return perimeter

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

vertice1 = Point(0, 0)
vertice2 = Point(1, 0)
vertice3 = Point(0, 1)

triangle = Triangle(vertice1, vertice2, vertice3)

print(triangle.perimeter())
