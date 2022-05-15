MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def print_report():
    """Prints current amounts of water, milk, coffee, and money"""
    for item in resources:
        print(f"{item.title()}: {resources[item]}")
    print(f"Money: {money}")


def check_resources_sufficient(water_needed, milk_needed, coffee_needed):
    """Returns true if there is enough water, milk, and coffee to make the drink"""

    def not_enough(item):
        print(f"Sorry, there is not enough {item}.")
        return False

    if resources["water"] < water_needed:
        not_enough("water")
    elif resources["milk"] < milk_needed:
        not_enough("milk")
    elif resources["coffee"] < coffee_needed:
        not_enough("coffee")
    return True


def process_coins():
    """Asks user for coins and calculates the amount"""
    print("Please insert coins.")
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickels = int(input("How many nickels do you have? "))
    pennies = int(input("How many pennies do you have? "))
    value = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return value


def check_success(item, amount):
    """Check to make sure the user gave sufficient funds"""
    global money
    cost = MENU[item]["cost"]
    if cost > amount:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cost <= amount:
        money += cost
        if cost < amount:
            change = amount - cost
            change = round(change, 2)
            print(f"Here is ${change} in change")
        return True


def make_coffee(customer_choice):
    """Deduct from ingredients and add money"""
    water_amount = MENU[customer_choice]["ingredients"]["water"]
    coffee_amount = MENU[customer_choice]["ingredients"]["coffee"]
    if "milk" in MENU[customer_choice]["ingredients"]:
        milk_amount = MENU[customer_choice]["ingredients"]["milk"]
    else:
        milk_amount = 0

    resources["water"] -= water_amount
    resources["coffee"] -= coffee_amount
    resources["milk"] -= milk_amount


coffee_on = True


def coffee_machine():
    """Use the coffee machine"""
    global coffee_on
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_choice == "off":
        coffee_on = False
    elif customer_choice == "report":
        print_report()
        coffee_machine()
    else:
        water_amount = MENU[customer_choice]["ingredients"]["water"]
        coffee_amount = MENU[customer_choice]["ingredients"]["coffee"]
        if "milk" in MENU[customer_choice]["ingredients"]:
            milk_amount = MENU[customer_choice]["ingredients"]["milk"]
        else:
            milk_amount = 0

        check_resources_sufficient(water_amount, milk_amount, coffee_amount)
        amount_given = process_coins()
        if check_success(customer_choice, amount_given):
            make_coffee(customer_choice)
            print(f"Here is your {customer_choice}. Enjoy!")
        coffee_machine()


while coffee_on:
    coffee_machine()
