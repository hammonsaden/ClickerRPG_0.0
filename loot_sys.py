import random



class Loot_Sys:
    def __init__(self):
        #self.Player = Player
        #self.Enemy = Enemy
        self.loot_table = {
    "Twisted Wooden Staff" : {"Intellect" : 2, "Damage" : 1, "Selling Price" : 10, "AC" : 0, "Rarity" : "Common"},
    "Wooden Bark Helmet" : {"Intellect" : -1, "Damage" : 0, "Selling Price" : -5, "AC" : 1, "Rarity" : "Common"},
    "Rusty Ritual Dagger" : {"Intellect" : 1, "Damage" : 1, "Selling Price" : 7, "AC" : 0, "Rarity" : "Common"},
    "Worn Leather Boots" : {"Intellect" : 1, "Damage" : 1, "Selling Price" : 15, "AC" : 1, "Rarity" : "Uncommon"},
    "Chipped Wooden Shield" : {"Intellect" : -1, "Damage" : 0, "Selling Price" : 4, "AC" : 2, "Rarity" : "Common"},
    "Shining Copper Ring" : {"Intellect" : 2, "Damage" : 1, "Selling Price" : 18, "AC" : 1, "Rarity" : "Rare"}
}
        self.drop_rates = {'Common' : 0.80, "Uncommon" : 0.15, "Rare" : 0.05}

    def roll_for_rarity(self):
        # Generate a random number between 0 and 1
        roll = random.random()
        print(roll)
        # Determine the rarity based on the drop rates
        for rarity, rate in self.drop_rates.items():
            if roll < rate:
                return rarity

    def generate_loot(self, Player):
        # Roll for rarity
        rarity = self.roll_for_rarity()

        # Filter loot items based on the rolled rarity
        eligible_loot = {item: info for item, info in self.loot_table.items() if info['Rarity'] == rarity}

        # If there are eligible loot items, randomly select one
        if eligible_loot:
            selected_item = random.choice(list(eligible_loot.keys()))
            Player.add_to_inventory(selected_item)
        else:
            print("Error Looting!")

