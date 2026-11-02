#Program to calculate average percentage 
course1 = int(input("Enter marks of course 1: "))
course2 = int(input("Enter marks of course 2: "))
course3 = int(input("Enter marks of course 3: "))
course4 = int(input("Enter marks of course 4: "))
course5 = int(input("Enter marks of course 5: ")) #calculate total marks
total_marks = course1 + course2 + course3 + course4 + course5 #calculate avg
average=total_marks/5 #calculate percentage
percentage=(total_marks*100)/250 #display results
print("Total Marks:", total_marks) 
print("Average:",average) 
print("Percentage:",percentage,"%")