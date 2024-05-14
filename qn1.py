res=[
    ["chi",20.0],
    ["beta",50.0],
    ["alpha",50.0]
    ]

# Step 1: Find the second lowest grade
grades = set([student[1] for student in res])
print(grades)
second_lowest_grade = sorted(grades)[1]
print(second_lowest_grade)

# Step 2: Collect the names of students with the second lowest grade
students_with_second_lowest = [student[0] for student in res if student[1] == second_lowest_grade]

# Step 3: Sort the names alphabetically
students_with_second_lowest.sort()

# Step 4: Print each name on a new line
for student in students_with_second_lowest:
    print(student)