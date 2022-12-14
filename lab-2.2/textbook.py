"""
Program Name: textbook.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Determine the cost of a student's textbooks.
Dates: 2022-09-23 - File created.
"""

# Ask the user how many textbooks they need
print("How many textbooks do you have to buy? ", end="")
# Input loop w/ validation
while True:
    books_needed = input()
    # Checks if input satisfies our conditions
    if books_needed.isnumeric() is False:
        print("Enter a whole, positive number, no spaces: ", end="")
    else:
        # Cast books_needed as int and break loop
        books_needed = int(books_needed)
        break

total_cost = 0.0

# Sum the book costs
for book in range(books_needed):
    # Another input loop
    while True:
        price = input(f"Enter price in whole dollars for book #{book + 1}: ")
        # Validation
        if price.isnumeric() is False:
            print("I said <<WHOLE DOLLARS>>, chump!!")
        else:
            total_cost += float(price)
            break
    print(f"\tRunning subtotal = ${total_cost:<.2f}.")

# That's all folks!
print(f"Grand total = ${total_cost:<.2f}.")
