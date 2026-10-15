import sys
import random

number = random.randint(1,5)

print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 5 :")
print("if you want to exit the game, please press Ctrl+C")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 5:
        print("Enter a number between 1 and 5.")
        continue

    attempts += 1

    if guess == number:
        print("Congratulations! You guessed correctly!")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")