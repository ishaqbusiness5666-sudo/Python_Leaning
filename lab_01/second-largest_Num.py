print("If you want to stop then put input 0")
def sort_large_to_small(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr




def LargerNum(arr):
    largerNum = arr[0]
    for i in range(0,len(arr)):
        if(largerNum < arr[i]):
            largerNum= arr[i]

    return largerNum

arr = []
while(True):
    num =int(input("Enter Numbers : "))
    if(num == 0):
        break
    else:
        arr.append(num)
ArrangeArr=sort_large_to_small(arr)
if len(arr) > 0:
    print(ArrangeArr[1])
else:
    print("No numbers were entered.")