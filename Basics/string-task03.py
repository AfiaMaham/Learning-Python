# Task: Write a program to replace all occurrences of a given substring in a string with another substring.
# Example:
# Input: "I love programming" replace "love" with "hate"
# Output: "I hate programming"

Input = "I love programming"
if "love" in Input:
    output = Input.replace("love" , "hate")
print(output)