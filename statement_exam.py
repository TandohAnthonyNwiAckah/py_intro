"""
QUESTIONS
- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59

Example:

if grade = 87 then print('B')

"""
# SOLUTION
grade = range(0, 101)

print("The letter grade between 0 - 100 are : ")
for x in grade:
    print(f"{x}", end=',')
    if 89 < x < 101:
        print("Grade is A")
    elif 79 < x < 90:
        print("Grade is B")
    elif 69 < x < 80:
        print("Grade is C")
    elif 59 < x < 70:
        print("Grade is D")
    elif -1 < x < 60:
        print("Grade is F")
    else:
        print("Grade unknown")
