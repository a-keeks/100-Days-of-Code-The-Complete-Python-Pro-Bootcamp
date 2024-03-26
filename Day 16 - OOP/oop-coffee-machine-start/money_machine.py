class MoneyMachine:

    CURRENCY = "£"

    COIN_VALUES = {
            "10p": 0.1,
            "20p": 0.2,
            "50p": 0.05,
            "£1": 1,
            "£2": 2
        }
    
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def coins_accepted(self):
        """Returns coins that are accepted by the coffee machine"""
        coins_accepted = self.COIN_VALUES.keys()
        coins_accepted = [coin for coin in coins_accepted]
        coins_accepted_str = ', '.join(coins_accepted[0:len(coins_accepted)-1]) + " and " + coins_accepted[-1]
        return f"Please Note: This machine only accepts {coins_accepted_str} coins."


    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin} coins?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False


