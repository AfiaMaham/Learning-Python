# Continue Statement Assignments

# Skip Multiples: Write a program to print all numbers from 1 to 20,
#  but skip the multiples of 3 using the continue statement.

for i in range (1,21):
    if i % 3 == 0:
        continue
    else:
        print(i)


# Odd Numbers Only: Write a program to print all odd numbers between 
# 1 and 30 using a loop and the continue statement.

for i in range (1,31):
    if i % 2 != 0:
         print(i)
    else:
         continue
       

