def chinkNum(num):
    if(num == 0):
        return "The number is zero."
    elif(num < 0):
        return "The number is negative."
    else:
        return "The number is positive."

Num = int(input("Type a number: "))

print(chinkNum(Num))

