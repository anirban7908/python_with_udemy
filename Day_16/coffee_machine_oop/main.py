from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

class_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
all_items  = class_menu.get_items()

user_input = input(f"What would you like? ({all_items}): ")
if user_input == 'off':
        is_on = False
elif user_input == 'report':
    coffee_maker.report()
else:
    chosen_drink = class_menu.find_drink(user_input)
    print(chosen_drink.__dict__)
    if coffee_maker.is_resource_sufficient(chosen_drink):
        print(coffee_maker.is_resource_sufficient(chosen_drink))
        if money_machine.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee( chosen_drink)

