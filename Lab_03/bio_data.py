Write a program to print a student’s bio data having his/her Date of birth, Roll no, Section, Percentage and grade of matriculation and Intermediate. All the fields should be entered from the console at run time. 
Here is a Python program that prompts the user to enter their bio data, including Date of Birth, Roll Number, Section, Percentage, and Grade for both Matriculation and Intermediate. The program then prints the entered information in a formatted manner.
 
name = input("Enter your name: ")
dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
roll_no = input("Enter your Roll Number: ") 
section = input("Enter your Section: ")
matric_percentage = float(input("Enter your Matriculation Percentage: "))
matric_grade = input("Enter your Matriculation Grade: ")
intermediate_percentage = float(input("Enter your Intermediate Percentage: "))
intermediate_grade = input("Enter your Intermediate Grade: ")
print("\nStudent Bio Data")
print("-------------------")
print(f"Name: {name}")
print(f"Date of Birth: {dob}")
print(f"Roll Number: {roll_no}")
print(f"Section: {section}")
print(f"Matriculation Percentage: {matric_percentage}%")
print(f"Matriculation Grade: {matric_grade}")
print(f"Intermediate Percentage: {intermediate_percentage}%")
print(f"Intermediate Grade: {intermediate_grade}")S