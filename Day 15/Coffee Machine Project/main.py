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

<<<<<<< HEAD
profit = 0

def report(data):
    """Retuen the report of the inventory"""
    for items, value in data.items():
        print(f"{items}: {value}")
    
    print(f"Money: ${profit}")

def check_resources(drink):
    """return true if the proper ingredients are available in the inventory and false if the ingredients are less"""
    ingredients = drink['ingredients']

    for items in ingredients:
        if ingredients[items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    
    return True


def process_coins():
    """Check if the amount paid by customer is okay for the drink"""
    print('Please insert coins!')
    total = int(input('How many quaters?: ')) *0.25
    total += int(input('How many dimes?: ')) *0.1
    total += int(input('How many nickles?: ')) *0.05
    total += int(input('How many pennies? ')) *0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """return true if the payment is proper or more and false id the payment is less! """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the change: ${change}")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def proces_drink(drink_name, order_ingredients):
    """Deduced the ingredients from the inventory"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    
    print(f'Here is you {drink_name}')

is_on = True

while is_on:
    user_input = input(f"What would you like? (espresso/latte/cappuccino): ")

    if user_input == 'off':
        is_on = False
    elif user_input == 'report':
        report(resources)
    else:
        chosen_drink = MENU[user_input]

        if check_resources(chosen_drink):
            payment = process_coins()
            if is_transaction_successful(payment, chosen_drink['cost']):
                proces_drink(user_input, chosen_drink['ingredients'])
=======
>>>>>>> origin/master
