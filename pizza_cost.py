#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Sep. 28, 2022
# This program calculates the cost of a pizza order.

import constants


def main():
    # input
    pizza_count = int(input("Enter the number of pizzas you are ordering: "))
    print("")
    diameter = float(input("Enter the diameter of the pizza(s) in inches: "))
    print("")
    # process
    subtotal = (
        constants.LABOUR * pizza_count
        + constants.RENTAL * pizza_count
        + constants.INGRED * diameter
    )
    # output
    total = subtotal * (constants.HST + 1)

    print("The total cost of the order is ${:,.2f}".format(total))


if "__main__" == __name__:
    main()
