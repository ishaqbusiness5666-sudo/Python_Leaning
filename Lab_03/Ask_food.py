# Write a program that asks the user what kind of food they would like. Print a message about that food, such as “Let me see if I can find you a Chowmein”. Food name must be in uppercase. (hint: use upper( ) for food name) 

food = input("What kind of food would you like? ")
food_upper = food.upper()
print(f"Let me see if I can find you a {food_upper}.")
print(f"Enjoy your {food_upper}!")
