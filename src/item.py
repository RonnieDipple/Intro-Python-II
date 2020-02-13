class Item:
    # Base class
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\Value: "


class WitcherCoins(Item):
    def __init__(self, amount, name, description, value):
        self.amount = amount
        super().__init__("WitcherCoins", "Coins to toss at your witcher".format(str(self.amount)), self.amount)


class Weapon(Item):

    def __init__(self, name, description, value, damage):
        raise NotImplementedError(f"Do not create raw Weapon objects ")
        self.damage = damage
        super().__init__(name, description, value)

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class GesheftSilverSword(Weapon):
    def __init__(self):
        super().__init__("Gesheft Silver Sword",
                         "The Ultimate Weapon, with your bad breath being a close second",
                         50,
                         50)


class EnchantedShotgun(Weapon):
    def __init__(self):
        super().__init__("Enchanted Shotgun, Very powerful, If your name is Ash this must bring back memories")




