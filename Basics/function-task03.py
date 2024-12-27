# Table of a Number
# Write a function that takes a number as input and prints its multiplication table.

def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

num = int(input("Enter number: "))
table(num)