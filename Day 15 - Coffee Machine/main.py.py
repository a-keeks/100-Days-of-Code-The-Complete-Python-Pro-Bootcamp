import os

def clear():
    os.system('cls')

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

options = []
for item, value in MENU.items():
    options.append(item)
options = '/'.join(options[0:len(options)-1]) + "/" + options[-1]

COIN_VALUES = {
        "10p": 0.1,
        "20p": 0.2,
        "50p": 0.5,
        "£1": 1,
        "£2": 2
    }

coins_accepted = list(COIN_VALUES.keys())
coin_values = list(COIN_VALUES.values())
coins_accepted_str = ', '.join(coins_accepted[0:len(coins_accepted)-1]) + " and " + coins_accepted[-1] #converts prev list to string so machine can let user know what coins are avail
amounts = []
funds = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
} # starting resources

def switch_off():
    print("Powering off ...")
    clear()
    

def is_resource_sufficient(order_ingredients):
    """Checks if there is enough of each ingredient for selected drink"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}. Please choose another drink: ")
            return False
    return True

result = []
def process_coins():
    global funds
    print(f"Please insert your coins.")
    for coin in coins_accepted:
        amount = int(input(f"How many {coin} coins?: "))
        amounts.append(amount)

    for x in range(len(coin_values)):
        funds += coin_values[x] * amounts[x]
    return funds

def sufficient_money(funds, price):
    """Checks if there is enough money for the selected drink"""
    if funds >= price:
        change = round(funds - price, 2)
        print (f"Here is £{change:.2f} in change.")
        make_drink(choice, drink["ingredients"])
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False    

def make_drink(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


def ingredient_report():
    """Prints amount of each resource left in machine"""
    report = input("Would you like to see a report of the amount of water, milk and coffee left in the machine? Type y or n: ").lower()
    if report == "y":
        for key, value in resources.items():
            print(key.title(), ":", value)


machine_on = True
while machine_on:
    buy_drink = input("Would you like to buy a drink? Type 'y' to see the options, 'n' to switch off the machine or 'report' to see a report of the ingredients left in the machine: ").lower()

    if buy_drink == "report":
        for key, value in resources.items():
            print(key.title(), ":", value)
            
    if buy_drink == "y":
        choice = input(f"What would you like? ({options})?\n").lower()
        drink = MENU[choice]
        price = drink.get("cost")
        print(f"That will be £{price:.2f}")
        print(f"Please Note: This machine only accepts {coins_accepted_str} coins.")

        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            sufficient_money(payment, price)
            ingredient_report()
            
    if buy_drink == "n":
        switch_off()
        machine_on = False
        
                


                

                    
            


