# Here, there are two similar classes: Rectangle and Square.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length    
# You can use them as below:
# square = Square(4)
# square.area()
# rectangle = Rectangle(2,4)
# rectangle.area()    
# By using inheritance, you can reduce the amount of code you write
# while simultaneously reflecting the real-world relationship between rectangles and squares: