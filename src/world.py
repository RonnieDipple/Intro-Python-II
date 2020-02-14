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

    def modify_player(self, player):  # abstract raises an exception without this and I have no idea why, not good
        pass


class EnemyTile(MapTile):
    # Place this anywhere on the map and enemies will randomly spawn, need to figure out a way to do that on preexisting maps

    def __init__(self, x, y):
        r = random.random()
        # The random() method module returns a decimal from 0.0 to 1.0 which means the player will encounter the care take in 50% rooms/tiles
        if r < 0.50:
            self.enemy = enemies.TheCareTaker()
            self.alive_text = "The Care Taker appears out of nowhere " \
                              " to take care of you "
            self.dead_text = "The Care Taker is no more " \
                             "he is as dead as Jacks love life "
        elif r < 0.80:
            self.enemy = enemies.TheToadPrince()
            self.alive_text = "You feel something moist hit the back of your head " \
                              "You turn to see a frog wearing royal robes and a crown with his mouth open " \
                              "He looks hungry "

            self.dead_text = "A crown lays on the floor on it's side " \
                             "What looks to be a half melted frog's body begins to hiss "

        elif r < 0.95:
            self.enemy = enemies.TheLocustSwarm()
            self.alive_text = "You hear a distant hum approaching " \
                              "Out the corner of your eye you see something move " \
                              "A cloud of darkness comes roaring towards you "

            self.dead_text = "Dozens of little bodies lay on the ground twitching " \
                             "You move a little and hear a crunch "
        else:
            self.enemy = enemies.Amarok()
            self.alive_text = "You hear a scratch " \
                              "You feel a gust of wind " \
                              "You hear a growl and feel his breath on your neck "

            self.dead_text = "You have done what many have failed to do " \
                             "Amarok lays dead " \
                             "But for how long? "

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


# Starting tile
class OutsideTile(MapTile):
    def description(self):
        return "Outside A Cave Entrance"

    def intro_text(self):
        return """"North of you, the cave mount beckons"""


# Quest tiles
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


# Future end game point?
class TreasureTile(MapTile):
    def description(self):
        return """"Treasure Chamber"""

    def intro_text(self):
        return """"You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""


####How the DSL Below works, first the dsl is validated and if it is invalid a syntaxError occurs,
# then the DSL get's split into lines and the empty lines are removed, the triple quote syntax world dsl """ is necessary to do this
# the last part creates the world  to long to explain, long form version available in your browser, this makes building large numbers of rooms trivial

world_dsl = """
|OT|TT|ET|ET|ET|
|FT|  |  |  |ET|
|ET|NT|ET|  |ET|
|ET|  |ET|ET|ET|
|ST|  |ET|  |ET|
"""

#Map above is hardcore mode you will die
# |OT|TT|
# |FT|NT|ET|
# |ST|ET|

def is_dsl_valid(dsl):
    # This checks if the DSL like above is correct
    # In this case the DSL must have a starting tile and a Victory tile
    if dsl.count("ST") != 1:
        return False
    if dsl.count("TT") == 0:
        return False
    lines = dsl.splitlines()  # Splits the strings
    lines = [l for l in lines if l]  # if l is shorthand for if l!=
    pipe_counts = [line.count("|") for line in lines]  # Counts the pipes in a row
    for count in pipe_counts:
        if count != pipe_counts[0]:  # If any condition fails it returns false
            return False
    return True

# here this dictionary maps the dsl abreviations to file types those types are just referenced and not intstantiated
tile_type_dict = {"TT": TreasureTile,
                  "ST": OutsideTile,
                  "FT": FoyerTile,
                  "OT": OverlookTile,
                  "NT": NarrowTile,
                  "ET": EnemyTile,
                  "  ": None}


def parse_world_dsl():
    if not is_dsl_valid(
            world_dsl):  # checks if dsl world is valid, basically looking for a corrupted world seed like minecraft
        raise SyntaxError("DSL is invalid!")  # If not valid returns
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]  # similar function to the one in is_dsl_valid above

    for y, dsl_row in enumerate(
            dsl_lines):  # looking for y also reminder Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            row.append(tile_type(x, y) if tile_type else None)  # where the magic happens
        world_map.append(row)


world_map = []


def tile_at(x, y):
    if x < 0 or y < 0:  # if x < 0 or y < 0 handles coordinates smaller than the bounds of the map
        return None
    try:
        return world_map[y][
            x]  # The world_map[y] part selects the row of the map and adding [x] selects the specific cell in that row
    except IndexError:  # Catching IndexError will handle the situation where we pass in a coordinate greater than the bounds of the map
        return None

# Redundant due to DSL
# Actual map vital to the game
# world_map = [

# This map is vital for traversing the world, to create new tiles create a new tile class then add that class here and with it's coordinates
# [OverlookTile(0, 0), TreasureTile(1, 0), None],
# [FoyerTile(0, 1), NarrowTile(1, 1), EnemyTile(2,1)],
# [OutsideTile(0, 2), EnemyTile(1,2), None]

# ]


# coordinates

# Overlook = 0.0     Treasure = 1.0
#    ↓ ↑                ↓ ↑
#    ↓ ↑     ←←←←←      ↓ ↑
# Foyer = 0.1 →→→→→ Narrow = 1.1
#    ↓ ↑
#    ↓ ↑
# outside = 0.2

# This finds the tile coordinates so the player can move

# |OT|TT|
# |FT|NT|ET|
# |ST|ET|
