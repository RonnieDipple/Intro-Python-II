import random

from src import enemies
from src.enemies import *
from src.enemies import Enemy


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead of this")

    def modify_player(self, player):
        pass


class OutsideTile(MapTile):
    def description(self):
        return "Outside A Cave Entrance"

    def intro_text(self):
        return """"North of you, the cave mount beckons"""

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.TheCareTaker
            self.alive_text = "The Care Taker appears out of nowhere, to take care of you"
            self.dead_text = "The Care Taker is no more, he is as dead as Jacks love life"

        super().__init__(x, y)

        def intro_text(self):
            text = self.alive_text if self.enemy.is_alive() else self.dead_text
            return text

        def modify_player(self, player):
            if self.enemy.is_alive():
                player.hp = player.hp - self.enemy.damage
                print("Enemy does {} damage. You have {} HP remaining.".
                      format(self.enemy.damage, player.hp))


class FoyerTile(MapTile):
    def description(self):
        return """"A Foyer, common now your wasting my time an yours I mean what was you expecting me to say?"""

    def intro_text(self):
        return """Dim light filters in from the south. Dusty
passages run north and east."""


class OverlookTile(MapTile):
    def description(self):
        return """"Grand Overlook is a cliff, can you feel the call of the void?"""

    def intro_text(self):
        return """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""


class NarrowTile(MapTile):
    def description(self):
        return """"It is a Narrow Passage, I know super exciting, 
        well it would be if a man with a mask chased you down it with a chainsaw!"""

    def intro_text(self):
        return """"The narrow passage bends here from west
to north. The smell of gold permeates the air."""


class TreasureTile(MapTile):
    def description(self):
        return """"Treasure Chamber"""

    def intro_text(self):
        return """"You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""





world_map = [

    # This map is vital for traversing the world, to create new tiles create a new tile class then add that class here and with it's coordinates
    [OverlookTile(0, 0), TreasureTile(1, 0), None],
    [FoyerTile(0, 1), NarrowTile(1, 1), None],
    [OutsideTile(0, 2), None, None]

]


# coordinates

# Overlook = 0.0     Treasure = 1.0
#    ↓ ↑                ↓ ↑
#    ↓ ↑     ←←←←←      ↓ ↑
# Foyer = 0.1 →→→→→ Narrow = 1.1
#    ↓ ↑
#    ↓ ↑
# outside = 0.2

def tile_at(x, y):
    if x < 0 or y < 0:  # if x < 0 or y < 0 handles coordinates smaller than the bounds of the map
        return None
    try:
        return world_map[y][
            x]  # The world_map[y] part selects the row of the map and adding [x] selects the specific cell in that row
    except IndexError:  # Catching IndexError will handle the situation where we pass in a coordinate greater than the bounds of the map
        return None
