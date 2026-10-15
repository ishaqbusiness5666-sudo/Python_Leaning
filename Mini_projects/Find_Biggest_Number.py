print("If you want to stop then put input 0")
def LargerNum(arr):
    largerNum = arr[0]
    for i in range(0,len(arr)):
        if(largerNum < arr[i]):
            largerNum= arr[i]

    return largerNum

arr = []
while(True):
    num = int(input("Enter Numbers : "))
    if(num == 0):
        break
    else:
        arr.append(num)

if len(arr) > 0:
    print(LargerNum(arr))
else:
    print("No numbers were entered.")