## Goal: Make an Expense tracker that allows a user to input a series of expenses, store them in a list, and then calculate the total spent.
from numpy.f2py.crackfortran import true_intent_list

## Initialize an empty list
expenses = []

## Start a loop: so the user can enter as many items as they want
while True:
    user_input = input("Enter expense amount (or 'done'): ")

    #Check if the user stops
    if user_input.lower() == 'done':
        break

    # Convert input to a number and add to list
    try:
        amount = float(user_input)
        expenses.append(amount)
    except ValueError:
        print("Invalid input. Enter a number or 'done'.")

## Ask the user for a budget
budget = int(input("How much would you like to have as your budget? "))

# Final calculation
total = sum(expenses)
item_count = len(expenses)

print("\n-----Summary-----")
print(f"Total items: {item_count}")
print(f"Total spent: ${total:.2f}")
print(f"Budget: ${budget:.2f}")

# Check if the user went over their budget
if total > budget:
    over_by = total - budget
    print(f"You went OVER your budget by ${over_by:.2f}")
elif total < budget:
    under_by = budget - total
    print(f"Congrats, you are UNDER your budget by ${under_by:.2f}")
else:
    print("You exactly met your budget!")

print("\n---Itemized Expenses---")
for x in expenses:
    print(f"- ${x}")
