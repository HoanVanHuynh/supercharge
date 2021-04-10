class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  

class SquarePrism(Square):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def face_area(self):
        base_area = super().area()
        lateral_area = self.side * self.height
        return base_area, lateral_area 
    
    def area(self):
        base_area = super().area()
        lateral_area = self.side * self.height
        return 2 * base_area + 4 * lateral_area

class Cube(SquarePrism):
    def __init__(self, side):
        super().__init__(side=side, height=side)

    def face_area(self):
        return super(SquarePrism, self).area()
    
    def area(self):
        return super().area()
c = Cube(3)
print(c.face_area())
print(c.area())