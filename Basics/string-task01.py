
# type: ignore # Task: Write a function that removes all spaces from a string.
# Example:
# Input: " Hello World "
# Output: "HelloWorld"

var = "Hello World "

for i in var:
    if i.isspace():
        continue
    else:
        print(i,end="")

