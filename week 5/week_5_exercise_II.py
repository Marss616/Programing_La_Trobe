class CoinPurse:
    def __init__(self, owner):
        self.owner = owner
        self.coins = 0

    def add_coin(self, coins):
        if coins > 0:
            self.coins += coins  # Update self.coins

    def print_information(self):
        print(self.owner, "has", self.coins, "cents")


# Example usage:
# The code below is your provided snippet.
        
name = input('Enter owner name: ')
purse = CoinPurse(name)
while True:
    value = int(input('Enter coin value (cents): '))
    if value <= 0:
        break
    purse.add_coin(value)
purse.print_information()


