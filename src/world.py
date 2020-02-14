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

#Starting tile
class OutsideTile(MapTile):
    def description(self):
        return "Outside A Cave Entrance"

    def intro_text(self):
        return """"North of you, the cave mount beckons"""


class EnemyTile(MapTile):
    #Place this anywhere on the map and enemies will randomly spawn, need to figure out a way to do that on preexisting maps
    def description(self):
        return "A scary place who knows what lurks here"
    def __init__(self, x, y):
        r = random.random()
        #The random() method module returns a decimal from 0.0 to 1.0 which means the player will encounter the care take in 50% rooms/tiles
        if r < 0.50:
            self.enemy = enemies.TheCareTaker()
            self.alive_text = "The Care Taker appears out of nowhere" \
                              " to take care of you"
            self.dead_text = "The Care Taker is no more" \
                             "he is as dead as Jacks love life"
        elif r < 0.80:
            self.enemy = enemies.TheToadPrince()
            self.alive_text = "You feel something moist hit the back of your head" \
                              "You turn to see a frog wearing royal robes and a crown with his mouth open" \
                              "He looks hungry"

            self.dead_text = "A crown lays on the floor on it's side" \
                             "What looks to be a half melted frog's body begins to hiss"

        elif r < 0.95:
            self.enemy = enemies.TheLocustSwarm()
            self.alive_text = "You hear a distant hum approaching" \
                              "Out the corner of your eye you see something move" \
                              "A cloud of darkness comes roaring towards you"

            self.dead_text = "Dozens of little bodies lay on the ground twitching" \
                             "You move a little and hear a crunch"
        else:
            self.enemy = enemies.Amarok()
            self.alive_text = "You hear a scratch" \
                              "You feel a gust of wind" \
                              "You hear a growl and feel his breath on your neck"

            self.dead_text = "You have done what many have failed to do" \
                             "Amarok lays dead" \
                             "But for how long?"

        super().__init__(x, y)

    # Intro Text
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    # Changes players life and hp status points
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining.")




#Quest tiles
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

#Future end game point?
class TreasureTile(MapTile):
    def description(self):
        return """"Treasure Chamber"""

    def intro_text(self):
        return """"You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""

#Actual map vital to the game
world_map = [

    # This map is vital for traversing the world, to create new tiles create a new tile class then add that class here and with it's coordinates
    [OverlookTile(0, 0), TreasureTile(1, 0), None],
    [FoyerTile(0, 1), NarrowTile(1, 1), EnemyTile(2,1)],
    [OutsideTile(0, 2), EnemyTile(1,2), None]

]


# coordinates

# Overlook = 0.0     Treasure = 1.0
#    ↓ ↑                ↓ ↑
#    ↓ ↑     ←←←←←      ↓ ↑
# Foyer = 0.1 →→→→→ Narrow = 1.1
#    ↓ ↑
#    ↓ ↑
# outside = 0.2

#This finds the tile coordinates so the player can move
def tile_at(x, y):
    if x < 0 or y < 0:  # if x < 0 or y < 0 handles coordinates smaller than the bounds of the map
        return None
    try:
        return world_map[y][
            x]  # The world_map[y] part selects the row of the map and adding [x] selects the specific cell in that row
    except IndexError:  # Catching IndexError will handle the situation where we pass in a coordinate greater than the bounds of the map
        return None
