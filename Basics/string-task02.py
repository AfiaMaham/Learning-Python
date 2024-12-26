# Reverse Words in a String:
# Task: Write a program that reverses each word in a string but keeps the word order intact.
# Example:
# Input: "hello world"
# Output: "olleh dlrow"

var = "Hello World "
x = var.split()
arr = []
for i in x:
    arr.append(i[::-1])
print(" ".join(arr))
