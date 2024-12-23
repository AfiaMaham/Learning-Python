# Count Even and Odd Numbers
# Count how many even and odd numbers are in an array.
# Example: Input: [1, 2, 3, 4, 5] → Output: Even: 2, Odd: 3

Input = [1, 2, 3, 4, 5]
even = 0
odd = 0

for i in Input:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"odd = {odd}")
print(f"even = {even}")