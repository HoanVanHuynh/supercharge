class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Cube(Square):
    def area(self):
        face_area = self.side * self.side
        return face_area * 6
    
    def volume(self):
        face_area = self.side * self.side 
        return face_area * self.side 

#Note: Since Cube class does not have an __init__() method,

class Cube1(Square):
    def area1(self):
        return self.area() * 6
    
    def volume(self):
        return self.area() * self.side

class Cube2(Square):
    def area(self):
        return super().area() * 6
    def volume(self):
        return super().area() * self.side  

class Cube3(Square):
    def area(self):
        return Square.area(self) * 6
    def volume(self):
        return Square.area(self) * self.side             
s = Square(3) 
print(s.area())       
c = Cube(3)        
print(c.volume())
c1 = Cube1(3)
print(c1.area1())
c2 = Cube2(3)
print(c2.volume())
c3 = Cube3(3)
print(c3.volume())