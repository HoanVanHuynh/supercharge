
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * self.length + 2 * self.width
# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length) # Here, you've used super() to call the __init__()
        # of the Rectangle class, allowing you to use it in the Square class without repeating code.

# Below, the core functionality remains after making changes:
# square = Square(4)
# square.area()        

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        #face_area = super().area()
        face_area = super()
        print(super())
        return face_area * self.length

# In the example below, you will create a class Cube that
# inherits from Square and extends the functionality of .area()
# (inherited from the Rectangle class through Square)
# to calculate the surface area and volume of a Cube instance:
# Now that you've built the classes, 
# Let's look at the surface area and volume of a cube with a side length of 3:
cube = Cube(3)
