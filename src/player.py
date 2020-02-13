# Write a class to hold player information, e.g. what room they are in
# currently.
from src import item


class Player:
    def __init__(self):
        self.inventory = [item.EnchantedShotgun,
                          'WitcherGold(1)',
                          'Crusty Bread']

        self.x = 0
        self.y = 2


# x, y aka dx and dy correspond to coordinates on the map
    def move(self, dx, dy):
        self.x += dx #dx, dy represent named parameters
        self.y += dy


    def move_north(self):
        self.move(0, -1)


    def move_south(self):
        self.move(0, 1)


    def move_east(self):
        self.move(1, 0)


    def move_west(self):
        self.move(-1, 0)

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))

        best_weapon = self.most_powerful_weapon()
        print(f"Your best weapon is you {best_weapon}")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None  # None is similar to null aka absence of value ake the abyss
        for item in self.inventory:
            try:  # The inventory will sometimes have non-weapons they don't have an attribute for damage,
                # so wrapping the code in a try and then error handling with AttributeError: pass which skips the comparison if
                # and therefore prevents a AttributeError: 'str' object has no attribute 'damage' exception
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon
