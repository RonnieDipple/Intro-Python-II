# Write a class to hold player information, e.g. what room they are in
# currently.
from src import items, world


class Player:
    def __init__(self):
        # Initial player items
        self.inventory = [items.EnchantedShotgun(),
                          items.GesheftSilverSword(),
                          items.CrustyBread()]
        # Player starts in this position/tile
        self.x = 0
        self.y = 2
        # players starting hp
        self.hp = 100

    def is_alive(self):
        return self.hp > 0

     # prints inventory
    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))

        best_weapon = self.most_powerful_weapon()
        print(f"Your best weapon is you {best_weapon}")

    # create health function needs to know what items the player has,
    # needs to display them for selection,
    # take user inout to select the item
    # Consume that item and remove it from inventory code can probably be reused to drop the item in rooms/tiles

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal:")
            print(f"{i}.{item}")

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print(f"Current HP: {self.hp}")
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, How dare you!")

    # Finds the most powerful weapon
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None  # None is similar to null aka absence of value ake the abyss
        for item in self.inventory:
            # The inventory will sometimes have non-weapons they don't have an attribute for damage,
            # so wrapping the code in a try and then error handling with AttributeError: pass which skips the comparison if
            # and therefore prevents a AttributeError: 'str' object has no attribute 'damage' exception
            try:
                if item.damage > max_damage:
                    best_weapon = item
                max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    # x, y aka dx and dy correspond to coordinates on the map
    # I felt more comfortable setting up movement using coordinates due to my Dyslexia
    def move(self, dx, dy):
        self.x += dx  # dx, dy represent named parameters
        self.y += dy

    def move_north(self):
        self.move(0, -1)

    def move_south(self):
        self.move(0, 1)

    def move_east(self):
        self.move(1, 0)

    def move_west(self):
        self.move(-1, 0)

        # Player attack method

    def attack(self):
        # Auto chooses best weapon
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print(f"You use {best_weapon.name} against {enemy.name} ")
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print(f"You killed {enemy.name}")
        else:
            print(f"{enemy.name} HP is {enemy.hp}")


