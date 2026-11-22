def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


terms = 7
series_sum = 0

for i in range(1, terms + 1):
    series_sum += i / fact(i)

result = series_sum * 2  # adds the first 7 terms twice
print("Sum of first 7 terms:", series_sum)
print("First 7 terms added twice:", result)