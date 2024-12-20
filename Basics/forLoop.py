# For Loop Assignments
# Sum of Numbers: Write a program to find the sum of all numbers from 1 to n, where n is entered by the user.

num = int(input("Enter the ending value of range: "))
sum = 0
for i in range (1,num+1):
    sum += i

print(f"The sum of numbers from 1 to {num} is {sum}")

