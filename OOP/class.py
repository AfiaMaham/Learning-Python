# 1. Creating a Class and Object
# Assignment:
# Create a class called Car that has the following attributes:
# make (string)
# model (string)
# year (integer)
# Create a method car_info() in the class that prints the car's make, model, and year.
# Create an object of the Car class with sample data and call the car_info() method to display the car's details.

class Car:
    make = "XYZ"
    Model = "ABC"
    year = "2024"
    def car_info(self):
        print("Make: ",self.make)
        print("Model: ",self.Model)
        print("Year: ",self.year)
obj = Car()
obj.car_info()