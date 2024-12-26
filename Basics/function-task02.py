# Find the Largest Number
# Write a function that takes three numbers and returns the largest among them.


def largest(num1,num2,num3):
    num = 0
    if(num1>num):
        num = num1
    if(num2>num):
        num=num2
    if(num3>num):
        num=num3
    return num

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
num3 = int(input("Enter third num: "))

print(largest(num1,num2,num3))