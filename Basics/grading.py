
# Grade Assignment
# Accept a percentage from the user and assign a grade:

# >= 90: A
# >= 75: B
# >= 50: C
# < 50: Fail

percentage = int(input("Enter your percentage: "))

if percentage >= 90:
    print("Your grade is A")
elif percentage >= 75:
    print("Your grade is B")
elif percentage >= 50:
    print("Your grade is C")
elif percentage < 50:
    print("Your have failed the exam")
else:
    print("Wrong input")