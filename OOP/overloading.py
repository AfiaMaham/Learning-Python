# Polymorphism (Method Overloading)
# Create a class Calculator with:
# A method add().
# If you pass two numbers to add(), it should return their sum.
# If you pass three numbers to add(), it should return their sum.
# Test the add() method with both two and three arguments.

class Calculator:
    def add(Self, num1, num2,num3 = 0):
        return num1 + num2 + num3
    
# obj = Calculator()
# print(obj.add(10,20,10))