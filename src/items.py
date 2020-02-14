class Weapon:

    def __init__(self, name, description, value, damage):
        raise NotImplementedError(f"Do not create raw Weapon objects ")

    def __str__(self):
        return self.name


class GesheftSilverSword(Weapon):
    def __init__(self):
        self.name ="Gesheft Silver Sword"
        self.description ="The Ultimate Weapon, with your bad breath being a close second",
        self.damage = 50
        self.value =50


class EnchantedShotgun(Weapon):
    def __init__(self):
        self.name ="Enchanted Shotgun"
        self.description = "Enchanted Shotgun, Very powerful, If your name is Ash this must bring back memories"
        self.damage = 30
        self.value = 100


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects")

    def __str__(self):
        return f"{self.name}(+{self.healing_value})"


# Using inheritence from Consumable you can now create food that heals and eventually potions etc
class CrustyBread(Consumable):

    def __init__(self):
        self.name = "Crusty Loaf"
        self.healing_value = 10
        self.value = 5

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60

# class WitcherCoins(self):
# def __init__(self, amount, name, description, value):
# self.amount = amount
# super().__init__("WitcherCoins", "Coins to toss at your witcher".format(str(self.amount)), self.amount)
