from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

    
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
import os

def clear():
    os.system('cls')

def switch_off():
    print("Powering off ...")
    clear()


machine_on = True
while machine_on:
    buy_drink = input(f"Would you like to buy a drink? Type 'y' to see the options, 'n' to switch off the machine or 'report' to see a report of the ingredients left in the machine: ")
    if buy_drink == "report":
        print(coffee_maker.report())

        buy_a_drink = input("Would you like to buy a drink? Type 'y' to see the options, 'n' to switch off the machine: ") 

    if buy_drink or buy_a_drink == "n" or "no":
        machine_on = False
        switch_off()

    if buy_drink or buy_a_drink == "y" or "yes":
        options = menu.get_items()
        choice = input(f"What would you like? ({options})")
        drink = menu.find_drink(choice)
        price = drink.cost
        print(f"That will be £{price:.2f}")
        print(money_machine.coins_accepted())
    
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




