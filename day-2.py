## Goal: Create a "Split the bill" calculator

# User Inputs

bill = float(input("How much was the total bill? "))
tip_percentage = int(input("How much would you like to tip in percentage? "))
people = float(input("How many people are paying? "))

# Calculate the total bill and tip amount

tip_amount = bill * (tip_percentage / 100)

total_bill = bill + tip_amount

## Calculate how much it will be for each person

total_per_person = total_bill / people

## Print final results
print("----------- Here is your bill summary -----------")
print(f"Total Bill before Tip: ${bill:.2f}")
print(f"Your Tip amount: ${tip_amount:.2f}")
print(f"The total bill with tip: ${total_bill:.2f}")
print(f"The total amount, split by person is ${total_per_person:.2f}")

