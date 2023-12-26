class CoinPurse:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.coins = []

    def add_coin(self, value):
        if value > 0:
            self.coins.append(value)

    def print_information(self):
        total_amount = sum(self.coins)
        print(f"Owner: {self.owner_name}")
        print(f"Total Coins: {len(self.coins)}")
        print(f"Total Value: {total_amount} cents")

# Usage of the class
name = input('Enter owner name: ')
purse = CoinPurse(name)

while True:
    try:
        value = int(input('Enter coin value (cents): '))
        if value <= 0:
            break
        purse.add_coin(value)
    except ValueError:
        print("Please enter a valid integer.")

purse.print_information()
