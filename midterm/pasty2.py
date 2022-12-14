"""
Program Name: pasty2.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Tabulate the costs of a series of Cornish pasties and generate an invoice.
Dates: 2022-10-18 - File created.
"""

import sys  # exit()


def main():
    # welcome user
    print("Welcome to Val's Semi-Cornish Pasties!\n")

    while True:
        # accept price and tip from user
        base_price, tip_percentage = inputs()
        # calculate transaction values
        tax, subtotal, tip, total = processing(base_price, tip_percentage)
        # generate invoice and display to user
        outputs(base_price, tax, subtotal, tip, tip_percentage, total)

        # goodbye!
        print("\nBon appetit!")

        # go again?
        print("Would you like to buy more of Val's lovely pasties? (y or n)")
        while True:
            command = str(input("$ "))
            if command == "y":
                break
            elif command == "n":
                print("Thanks for coming!")
                sys.exit()
            else:
                print(f"Huh? {command} don't mean much around here, fella.")


def inputs() -> (int, int):
    """
    Accepts input from the user specifying how much the pasties cost and the
    tip to be given to Val, our gracious chef.

    :returns: base_price, a 2-point precision float, the price of the pasties
              tip_percentage, a 1-point precision float, the tip percentage
                  to be added
    """
    base_price = get_pos_float(
        prompt="Enter the price of your pasties in $: ",
    )
    tip_percentage = get_pos_float(
        prompt="Enter the % of your subtotal you want to give to Val: ",
        invalid_msg="Invalid input, please try again.",
        precision=1,
    )
    return base_price, tip_percentage


def processing(
    base_price: float, tip_percentage: float
) -> (float, float, float, float):
    """
    Calculates some figures from the data the user provided.

    :param base_price: 2-point float, the base cost of the pasties
    :param tip_percentage: 1-point float, the percentage of the subtotal which
                           the user wants to tip
    :returns:
        tax: 2-point float, the tax to be added to base_price
        subtotal: 2-point float, base_price + tax
        tip: 2-point float, subtotal + (subtotal * (tip_percentage / 100))
        total: 2-point float, subtotal + tip
    """
    tax = round(base_price * 0.07025, 2)  # Minneapolis tax rate of 7.025%
    subtotal = base_price + tax
    tip_percentage /= 100
    tip = round(subtotal * tip_percentage, 2)
    total = subtotal + tip

    return tax, subtotal, tip, total


def outputs(base_price, tax, subtotal, tip, tip_percentage, total):
    """
    Prints the invoice for the pasty purchase.

    :param base_price: 2-point float, base price of the pasties
    :param tax: 2-point float, the tax to be added to subtotal
    :param subtotal: 2-point float, base_price + tax
    :param tip: 2-point float, tip to be added to subtotal
    :param tip_percentage: 1-point float, percentage of subtotal to tip
    :param total: 2-point float, grand total
    """
    # generate the line of the invoice that lists the tip percentage
    tip_string = "Tip @ {:.1f}%".format(tip_percentage)

    print("\nInvoice Due")
    print("{:<14}${:>10.2f}".format("Pasty price", base_price))
    print("{:<14}${:>10.2f}".format("Tax @ 7.025%", tax))
    print("{:<14}${:>10.2f}".format("Subtotal", subtotal))
    print("{:<14}${:>10.2f}".format(tip_string, tip))
    print("{:<14}${:>10.2f}".format("Total", total))


def get_pos_float(
    prompt="Enter a positive dollar amount: ",
    invalid_msg="Invalid input. Please enter in format $x.xx. Please.",
    precision=2,
) -> float:
    """
    Accepts a float from the user and validates it, asking again if the input
    is invalid according to the specified conditions.

    :param prompt: str, the prompt the user will see.
    :param invalid_msg: str, the message the user will see if their input isn't
                        a valid float.
    :param precision: int, the number of decimal places the input will be
                      rounded to, default is 2.
    :returns: a positive float
    """
    while True:
        try:
            i = float(input(prompt))
        except ValueError:
            print(invalid_msg)
            continue

        if i > 0.0:
            i = round(i, precision)
            return i
        else:
            print("This is a business, friend. You're gonna have to pay US.")


main()
