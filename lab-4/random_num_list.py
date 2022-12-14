"""
Program Name: random_num_list.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Provide a list of randomly selected numbers.
Dates: 2022-10-05 - File created.
"""

import sys     # exit()
import random  # randint()


def main():
    while True:
        intlist = inputs()  # provides us with a sorted list
        intlist_sum, intlist_min, intlist_max = processing(intlist)
        # take certain values from said list
        outputs(intlist, intlist_sum, intlist_min, intlist_max)
        # format the lists in printable form as desired

        # restart menu loop
        while True:
            choice = str(input("Care to give it another go? (y or n)"))
            if choice == "y":
                break
            elif choice == "n":
                print("Thanks for your time.")
                sys.exit()
            else:
                print("Come again?")


def inputs():
    intlist = list()
    print("How many integers should the computer pick for your list?")
    num_ints = get_pos_int()

    intlist = [random.randint(0, 9) for i in range(num_ints)]
    # populate the list with random integers in a list comprehension
    intlist.sort()
    return intlist
    # return a sorted intlist


def get_pos_int(prompt="Please enter a whole number: ") -> int:
    """Returns a positive int the user provides."""
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("A whole number greater than zero, if you please.")
            continue

        if number > 0:
            break
        else:
            print("POSITIVE, stay POSITIVE!")

    return number


def processing(intlist: list):
    # returns the sum of the list, the minimum, and the maximum respectively
    return sum(intlist), intlist[0], intlist[-1]


def outputs(intlist: list,
            intlist_sum: int,
            intlist_min: int,
            intlist_max: int):
    print(f"Here's your list of {len(intlist)} integers, randomly selected and sorted:")
    print(intlist)
    print("Here is your list printed with the \"shortcut\" method:")
    print(*intlist, sep=", ")
    print("Here is your list printed via a loop with total:")
    for i in intlist[:-1]:
        print(str(i) + " + ", end="")
    print(str(intlist_max) + " = " + str(intlist_sum))
    print(f"Your list minimum was {intlist_min} and maximum was {intlist_max} this time.")


print("Welcome to the random number list generating thingamabobber")
main()
