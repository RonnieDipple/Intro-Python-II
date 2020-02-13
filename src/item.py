class Item:
    # Base class
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\Value: "


class WitcherCoins(Item):
    def __init__(self, amount):
        self.amount = amount
        super(name="witcherCoins",
              description="Coins to toss at your witcher".format(str(self.amount)),
              value=self.amount).__init__()

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class GesheftSilverSword(Weapon):
    def __init__(self):
        super().__init__(name = "Gesheft Silver Sword",
                         description = "The Ultimate Weapon, with your bad breath being a close second",
                         value = 50,
                         damage = 50)

class EnchantedShotgun(Weapon):
    def __init__(self):
        super().__init__(name = "Enchanted Shotgun, Very powerful, If your name is Ash this must bring back memories")


