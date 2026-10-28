# Take the marks of 5 courses from the user and calculate the average and percentage, 	display the result: 
# 		Eachcourse=50 marks 
# 		Total_marks= course1+course2+course3+course4+course5 
# 		average=Total_marks/5 
# 		percentage=(Total_marks x 100)/250 

marks_list = []
for i in range(1, 6):
    marks = float(input(f"Enter marks for course {i} (out of 50): "))
    marks_list.append(marks)

total_marks = sum(marks_list)
average = total_marks / 5
percentage = (total_marks * 100) / 250
print(f"Total Marks: {total_marks}")
print(f"Average: {average}")
print(f"Percentage: {percentage}%")