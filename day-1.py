# Says hello to the world
print("hello, world")

# Asks the user what their name is
name = input("What is your name? ").strip().title()

# split user's name into first name and last name
first, last = name.split(" ")

#Says hello to the user
print (f"Hello, {first}")

# Another way you could say hello, maybe informally
nickname = input("What is your nickname?")

# Changes the default parameter of print of end= \n which creates a new line
print("That's a nice name " + nickname)

## Says hello to a friend, but sarcastically: backslashes or escape characters
friendship = input("Do you want to be \"friends?\"")

# Says goodbye in another way using the f and brackets
print(f"Goodbye, {name}!")