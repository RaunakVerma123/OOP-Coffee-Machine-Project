from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

while True:
    options = menu.get_items()
    order = input(f"What would you like? {options}: ")
    if order == "report":
        coffee_machine.report()
        money.report()
    elif order == "off":
        break
    else:
        drink = menu.find_drink(order)
        if drink is not None and coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
