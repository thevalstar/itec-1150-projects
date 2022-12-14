"""
Program Name: pasty1.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Tabulate the costs of a series of Cornish pasties and generate an invoice.
Dates: 2022-10-18 - File created.
"""

import sys  # exit()

# introduce the user to the program
print("Welcome to Val's Semi-Cornish Pasties!\n")

# input validation loops for the pasty price and tip
while True:
    try:
        base_price = float(input("Enter the price of your pasties in $.\n$ "))
    except ValueError:
        print("Invalid input. Please enter in format $x.xx. Please.")
        continue

    if base_price > 0.0:
        base_price = round(base_price, 2)
        break
    else:
        print("You're not all that, I'm not paying you to eat my pasties.")

while True:
    try:
        tip_percentage = float(input("Enter tip % of total that Val gets\n$ "))
    except ValueError:
        print("Invalid input. Please enter in decimal format a number greater than 0.")
        continue

    if tip_percentage > 0.0:
        tip_percentage = round(tip_percentage, 2)
        break
    else:
        print("These wait staff get paid so little as it is, you can't be asking them to pay YOU!")

# calculate tax, subtotal, and total
tax = round(base_price * 0.07025, 2)
subtotal = base_price + tax
tip_percentage /= 100
tip = round(subtotal * tip_percentage, 2)
# tip amount for invoice
tip_string = "Tip @ {:.1f}%".format(tip_percentage * 100)
total = subtotal + tip

# generate invoice
print("Invoice Due")
print("{:<14}${:>10.2f}".format("Pasty price", base_price))
print("{:<14}${:>10.2f}".format("Tax @ 7.025%", tax))
print("{:<14}${:>10.2f}".format("Subtotal", subtotal))
print("{:<14}${:>10.2f}".format(tip_string, tip))
print("{:<14}${:>10.2f}".format("Total", total))

# goodbye!
print("\nThanks for enjoying pasties from Minneapolis!")
sys.exit()
