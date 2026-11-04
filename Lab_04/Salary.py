YearOFExp= int(input("Years of Expriences : "))
print("1.For Master \n 2.For Bachelor \n")
Qualification = int(input("Enter Number : "))
if(YearOFExp<0 and (Qualification == 1 or Qualification==2 )):
    print("Enter correct Years of Experience and Qualifications !")
elif(YearOFExp>=10 and Qualification== 1 ):
    print("Your Salary is 150,000")
elif(YearOFExp>=10 and Qualification== 2):
    print("100,000")
elif(YearOFExp < 10 and Qualification == 1):
    print("Your Salary is 100,000")
elif(YearOFExp < 10 and Qualification == 2):
    print("Your Salary is 70,000")
else:
    print("Your are not qualified For This ")