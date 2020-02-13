class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead of this")


class OutsideTile(MapTile):
    def description(self):
        return """"Outside Cave Entrance"""

    def intro_text(self):
        return """"North of you, the cave mount beckons"""


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

    [OverlookTile, TreasureTile, None],
    [FoyerTile, NarrowTile, None],
    [OutsideTile, None, None]

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
    if x < 0 or y < 0:
        return None  # The world_map[y] part selects the row of the map and adding [x] selects the specific cell in that row
    try:  # Catching IndexError will handle the situation where we pass in a coordinate greater than the bounds of the map
        return world_map[y][x]  # And if x < 0 or y < 0 handles coordinates smaller than the bounds of the map
    except IndexError:
        return None
