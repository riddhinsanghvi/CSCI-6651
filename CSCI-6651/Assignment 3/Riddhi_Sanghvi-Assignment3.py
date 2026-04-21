""" Program #3 - GPA Calculator
This program collects grades for multiple students, stores them in a List of Lists,
converts them to numeric values, computes GPA for each student, and stores all GPAs in a separate list."""

# Dictionary for converting letter grades to numeric points
grade_points = {
    "A+": 5.0, "A": 4.7, "A-": 4.3,
    "B+": 4.0, "B": 3.7, "B-": 3.3,
    "C+": 3.0, "C": 2.7, "C-": 2.3,
    "D+": 2.0, "D": 1.7, "D-": 1.3,
    "F": 0.0
}

# Lists to hold all student grades and GPAs
students_grades = []  # List of Lists
students_gpa = []     # List of GPA values

student_number = 1

while True:
    # Prompt for input
    entry = input(f"Please enter the grades for Student #{student_number} "
                  "comma separated or 'Q' to quit entry > ").strip()

    # Quit if user enters Q
    if entry.upper() == "Q":
        break

    # Split the input into grades
    grades = [g.strip().upper() for g in entry.split(",")]

    # Validate grades
    valid = True
    for g in grades:
        if g not in grade_points:
            print(f"Invalid grade '{g}' entered. Please try again.")
            valid = False
            break

    if not valid:
        continue  # re-prompt for same student

    # Store grades in the List of Lists
    students_grades.append(grades)

    # Convert to numeric and calculate GPA
    numeric_grades = [grade_points[g] for g in grades]
    gpa = sum(numeric_grades) / len(numeric_grades)

    # Store GPA in GPA list
    students_gpa.append(round(gpa, 2))

    student_number += 1

# Display results
for i, gpa in enumerate(students_gpa, start=1):
    print(f"Student #{i} GPA: {gpa}")

# Show the List of Lists and GPA list (for clarity/debugging)
print("\nList of Lists (Grades):", students_grades)
print("GPA List:", students_gpa)
