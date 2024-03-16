MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]


def update_resources(coffee_type, water, milk, coffee):
    water = water - MENU[coffee_type]["ingredients"]["water"]
    milk = milk - MENU[coffee_type]["ingredients"]["milk"]
    coffee = coffee - MENU[coffee_type]["ingredients"]["coffee"]
    return water, milk, coffee


def return_change(money_given, actual_cost):
    change = money_given - actual_cost
    change = round(change, 2)
    print(f"Here is ${change} in change.")


def count_money(quarters, dimes, nickles, pennies):

    total_quarters_value = quarters * 0.25
    total_dimes_value = dimes * 0.10
    total_nickles_value = nickles * 0.05
    total_pennies_value = pennies * 0.01

    values = [total_quarters_value, total_dimes_value, total_nickles_value, total_pennies_value]

    total_amount = sum(values)
    return total_amount


# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

ask_again = True
while ask_again:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    print("Please insert coins.")
    cust_quarters = int(input("How many quarters?: "))
    cust_dimes = int(input("How many dimes?: "))
    cust_nickles = int(input("How many nickles?: "))
    cust_pennies = int(input("How many pennies?: "))


    # TODO 2: Check the user’s input to decide what to do next.

    if user_input == "espresso":
        if total_water >= 50 and total_coffee >= 18:
            espresso_cost = MENU["espresso"]["cost"]
            cust_money = count_money(cust_quarters, cust_dimes, cust_nickles, cust_pennies)

            if cust_money < espresso_cost:
                print("Sorry, not enough money")
            else:
                print("Enjoy your Espresso!")
                return_change(cust_money, espresso_cost)
                total_water, total_milk, total_coffee = update_resources(user_input, total_water, total_milk, total_coffee)

        else:
            print("Sorry, not enough resources!")

    if user_input == "latte":
        if total_water >= 200 and total_milk >= 150 and total_coffee >= 24:
            latte_cost = MENU["latte"]["cost"]
            cust_money = count_money(cust_quarters, cust_dimes, cust_nickles, cust_pennies)

            if cust_money < latte_cost:
                print("Sorry, not enough money")
            else:
                print("Enjoy your Latte!")
                return_change(cust_money, latte_cost)
                total_water, total_milk, total_coffee = update_resources(user_input, total_water, total_milk,
                                                                         total_coffee)

        else:
            print("Sorry, not enough resources!")

    if user_input == "cappuccino":
        if total_water >= 250 and total_milk >= 100 and total_coffee >= 24:
            cappuccino_cost = MENU["cappuccino"]["cost"]
            cust_money = count_money(cust_quarters, cust_dimes, cust_nickles, cust_pennies)

            if cust_money < cappuccino_cost:
                print("Sorry, not enough money")
            else:
                print("Enjoy your Cappuccino!")
                return_change(cust_money, cappuccino_cost)
                total_water, total_milk, total_coffee = update_resources(user_input, total_water, total_milk, total_coffee)

        else:
            print("Sorry, not enough resources!")


# TODO 3: The prompt should show every time action has completed, e.g. once the drink is dispensed.
# TODO 4: The prompt should show again to serve the next customer.



