import json

# Load JSON file
with open("student.json", "r") as f:
    students = json.load(f)

# Function to print all students
def print_student_list(student_list):
    for s in student_list:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")
    print()

print("Original Student List:")
print_student_list(students)

# Add your information
new_student = {
    "F_Name": "Noor",
    "L_Name": "Al Salihi",
    "Student_ID": 99999,
    "Email": "noor@example.com"
}

students.append(new_student)

print("Updated Student List:")
print_student_list(students)

# Write updated list back to student.json
with open("student.json", "w") as f:
    json.dump(students, f, indent=2)

print("student.json file updated.")

      

