
import random
import time
import sys

number = random.randint(1, 5)

print("Welcome to the guessing game!")
print("I'm choosing a number from 1 to 5.")

time.sleep(1)

start = time.perf_counter()
attempts = 0

while attempts < 3:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess < 1 or guess > 5:
        print("Choose a number from 1 to 5.")
        continue

    attempts += 1

    if guess == number:
        elapsed = time.perf_counter() - start
        print("You won, bro!")
        print("Attempts:", attempts)
        print("Time:", round(elapsed, 2), "seconds")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Game over!")
    print("The number was:", number)

print("Thanks for playing!")
  