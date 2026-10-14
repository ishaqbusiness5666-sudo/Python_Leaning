import sys

# grade calculator is a Python program that calculates the average score of a student based on the number of subjects and their respective scores. It then determines the corresponding grade based on the average score.
def calculate_grade(num):
    if(num > 100):
        return "Enter Number below the 100"
    if(num >= 80):
        return "A"
    elif(num >=70):
        return "B"
    elif(num >=60):
        return "C"
    elif(num >= 50):
        return "D"
    else:
        return "F"
# this function takes the number of subjects and an array to store the scores. It prompts the user to enter the score for each subject and appends it to the array. If the score is greater than 100 or less than 0, it prints an error message and exits the program.
def TakeAllSubj(num,arr):
    for i in range(1,num+1):
        score=int(input(f"Enter the subject {i} number : "))
    if(score > 100 or score < 0 ):
            print("Enter Number under 100")
            sys.exit() 
    arr.append(score)

# this function calculates the total sum of the scores in the array. It iterates through each score in the array, adds them up, and returns the total sum.
def total(arr):
    n=len(arr)
    sum = 0
    for i in range (0,n):
        sum += arr[i]
    return sum

# this function calculates the average score by dividing the total sum of scores by the number of subjects. It takes an array of scores as input, calculates the total using the total function, and then divides it by the length of the array to get the average. The average is then returned.
def Average(arr):
    numberOfVal=len(arr)
    SumofNum = total(arr)
    average = SumofNum/numberOfVal
    return average

# here i put the number of subjects and create an empty array to store the scores. Then, I call the TakeAllSubj function to get the scores from the user. After that, I calculate the average using the Average function and determine the grade using the calculate_grade function. Finally, I print the average and grade.
subjectNum=int(input("Enter the number of subjects : "))
marks=[]
TakeAllSubj(subjectNum,marks)
average = Average(marks)
Grade = calculate_grade(average)
print("Average is : " , average)
print("Grade is :" , Grade)
