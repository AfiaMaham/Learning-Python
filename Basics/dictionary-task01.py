# Update a Dictionary with Another Dictionary:

# Task: Write a function to update a dictionary with another dictionary. The second dictionary
#  should overwrite the values in the first dictionary for matching keys.
# Example:
# Input: {"a": 1, "b": 2}, update with: {"b": 3, "c": 4}
# Output: {"a": 1, "b": 3, "c": 4}

dict = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict.update(dict2)
print(dict)

