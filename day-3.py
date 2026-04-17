### Goal: make a coffee bot

# -------------------Inputs-------------------------------------------------
coffee_type = input("What kind of coffee can I get for you? ").strip().lower()
coffee_size = input(f"What size coffee can I get for you? ").strip().lower()

#--------------------Configuration-----------------------------------------
## Drinks Available
mocha = 4.00
black_coffee = 2.00
cortado = 3.50

## Size Percentage
small_percent = 0
medium_percent = 10
large_percent = 20

## Tax Rate
tax_rate = 6.25

## Initialize variables
coffee_order = 0
size_order = 0

#--------------------Selection Logic-------------------------------------

# Assigning the variable of coffee type based on the user's input
if coffee_type == "mocha":
    coffee_order = mocha
elif coffee_type == "black coffee":
    coffee_order = black_coffee
elif coffee_type == "cortado":
    coffee_order = cortado
else:
    print("I'm sorry we're out of that type of coffee.")

## Calculating the additional cost based on the size
if coffee_size == "small":
    coffee_size_addition = float(coffee_order * (small_percent / 100))
elif coffee_size == "medium":
    coffee_size_addition = float(coffee_order * (medium_percent / 100))
elif coffee_size == "large":
    coffee_size_addition = float(coffee_order * (large_percent / 100))
else:
    print("I'm sorry we dont have that size.")

#============================Final Calculations=========================
subtotal = coffee_order + coffee_size_addition
tax = subtotal * (tax_rate / 100)
total = subtotal + tax

print(f"\nYour total for a {coffee_size.capitalize()} {coffee_type.capitalize()} is: ${total:.2f}")


