YearOFExp= int(input("Years of Expriences : "))
print("1.For Master \n2.For Bachelor")
Qualification = int(input("Enter Number : "))
if(YearOFExp<0):
    print("Experience Must be a Positive Number!")
elif(Qualification != 1 and Qualification!=2 ):
    print("Enter Qualifications 1 or 2 only! ")
elif(YearOFExp>=10 and Qualification== 1 ):
    print("Your Salary is 150,000")
elif(YearOFExp>=10 and Qualification== 2):
    print("Your Salary is 100,000")
elif(YearOFExp < 10 and Qualification == 1):
    print("Your Salary is 100,000")
elif(YearOFExp < 10 and Qualification == 2):
    print("Your Salary is 70,000")
else:
    print("Your are not qualified For This ")