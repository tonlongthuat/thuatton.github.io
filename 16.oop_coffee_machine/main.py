from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drink=input('choose your drink: ')
drink=Menu()
coffee=CoffeeMaker()
coin=MoneyMachine()
is_on=True
# print(drink.get_items())
while is_on:
    option=drink.get_items()
    choice=input(f'which one you want to drink:{option} ')
    if choice == 'off' :
        is_on=False
    elif choice =='report':
        coffee.report()
        coin.report()
    else:
        customer_drink=drink.find_drink(choice)
        can_make=coffee.is_resource_sufficient(customer_drink)
        if can_make==True:
            coin.make_payment(customer_drink.cost)
            if True:
                coffee.make_coffee(customer_drink)



