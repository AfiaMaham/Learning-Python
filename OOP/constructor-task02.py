# 2. Rectangle Area and Perimeter
# Create a class Rectangle with attributes length and width. Initialize them using _init_. Create methods to:

# Calculate the area of the rectangle
# Calculate the perimeter of the rectangle

class Rectangle:
    def __init__(self, len, width):
        self.length = len
        self.width = width

    def Area(self):
        self.result = self.length * self.width
        return self.result
    def Perimeter(self):
        self.result = 2 * (self.length + self.width)
        return self.result
obj = Rectangle(2,2)
print("Area: ",obj.Area())
print("Perimeter: ",obj.Perimeter())