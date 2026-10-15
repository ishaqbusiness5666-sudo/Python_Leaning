import random
# it guesses number in 1 to 100
number = random.randint(1, 100)
print(number)

# it guesses color from a list of colors
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
color = random.choice(colors)
print(color)

# shuffle list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(numbers)

# random list in range 0 to 1
print("Random float between 0 and 1:", random.random())

