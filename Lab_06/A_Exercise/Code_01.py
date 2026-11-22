prompt="Enter 'quit' when you are finished."
prompt +="\nPlease enter the name of a city you have visited : "
while True:
    city = str(input(prompt))
    if city == 'quit':
        break
    else:
        print("I'd love to go to " , city.title() , "!")
