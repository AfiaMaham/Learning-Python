# Invert a Dictionary:

# Task: Write a function that inverts a dictionary. That is, the values become keys and the keys
#  become values.
# Example:
# Input: {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}

Input = {"a": 1, "b": 2, "c": 3}
output = {}
for key, value in Input.items():
    output.update({value : key})

print(output)