Starting = int(input("Enter first Number you want to start checking prime numbers from: "))
Ending = int(input("Enter Second Number where you want to Ending numbers from :"))

def is_prime(start,end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

is_prime(Starting, Ending)