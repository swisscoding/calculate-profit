#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

import colored

# decoration
print(colored.stylize("\n---- | Calculate the profit of your sales | ----\n", colored.fg("red")))

# user interaction
cost_price = float(input("What is the cost price of one product?\n"))
sell_price = float(input("\nWhat is the sell price of one product?\n"))
inventory = int(input("\nHow much of this product do you have?\n"))
sold = int(input("\nHow much products were sold?\n"))

# information for the calculation
information = {
    "cost_price": cost_price,
    "sell_price": sell_price,
    "inventory": inventory
}

def profit(dict, sold):
    return dict["sell_price"] * sold - dict["cost_price"] * dict["inventory"]

if sold == 1:
    print(f"\nOut of {inventory} products, {sold} was sold.")
else:
    print(f"\nOut of {inventory} products, {sold} were sold.")
amount = float(profit(information, sold))

if amount > 0:
    amount = colored.stylize(str(amount), colored.fg("green"))
    print(f"You made {amount}$ profit.\n")
elif amount < 0:
    amount = colored.stylize(str(amount), colored.fg("red"))
    print(f"You made {amount}$ loss\n")
else:
    amount = colored.stylize(str(amount), colored.fg("sandy_brown"))
    print(f"You are break even. {amount}$\n")
