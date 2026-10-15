import sys 
num = int(input("Enter how many number you want for analyaz : "))
if(num <= 0):
    print("Enter Number ")
    sys.exit()

list = []
for i in range(1,num+1):
    list.append(int(input(f"Enter num {i} : ")))
if(list[i] < 0 or list[i] > 100):
    print("Enter Number under 100")
    sys.exit()
if(num > 100):
    print("Enter Number below the 100")
    sys.exit()
if(num == 1):
    print("The largest number is : ",list[0])
    print("The smallest number is : ",list[0])
    print("The sum of the list is : ",list[0])
    print("The average of the list is : ",list[0])
    sys.exit()
    
def biggerNum(list):
    largerNum = list[0]
    for i in range(0,len(list)):
        if(largerNum < list[i]):
                largerNum= list[i]
    return largerNum

def SmallestNum(list):
    smallNum = list[0]
    for i in range(0,len(list)):
          if(smallNum > list[i]):
               smallNum = list[i]
    return smallNum

def SumOfList(list):
     sum = 0
     for i in range(0,len(list)):
          sum += list[i]
     return sum

def AverageOfList(list):
    total = len(list)
    sum = SumOfList(list)
    average = sum/total
    return average

def AllCallBack(list):
    print("The largest number is : ",biggerNum(list))
    print("The smallest number is : ",SmallestNum(list))
    print("The sum of the list is : ",SumOfList(list))
    print("The average of the list is : ",AverageOfList(list))

AllCallBack(list)