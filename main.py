from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

while True:
    options = menu.get_items()
    # For eg: latte, espresso...
    order = input(f"What would you like? {options}: ")
    if order == "report":
        coffee_machine.report()
        money.report()
    elif order == "off":
        break
    else:
        '''
        First we are checking if the drink ordered by the customer is available or not.If it is available,
        then we check if the resources to make the coffee are sufficient.We then ask the customer to make the payment,
        which when done will allow us to make and serve the coffee. '''
        drink = menu.find_drink(order)
        if drink is not None and coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
