# Simple Calculator
# Build a basic calculator that performs addition, subtraction, multiplication, or division based on user input.

val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
op = input("Enter the operation you want to perform: ")

if op == "+":
    print("Result of operation is: ",val1 + val2)
elif op == "-":
    print("Result of operation is: ",val1 - val2)
elif op == "*":
    print("Result of operation is: ",val1 * val2)
elif op == "/":
    print("Result of operation is: ",val1 / val2)
else:
    print("Invalid input")