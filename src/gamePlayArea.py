import sys
from textwrap import TextWrapper

from src import player, world
from src.player import Player
from src.room import Room
import src.enemies
import src.items
import src.world


# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def play():
    player1 = Player()
    wrapper = TextWrapper()
    wrapper.initial_indent = "* "
    while True:
        room = world.tile_at(player1.x, player1.y)
        print(room.intro_text())
        room.modify_player(player1)#controls hp loss and death
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            player1.move_north()
        elif action_input in ['s', 'S']:
            player1.move_south()
        elif action_input in['e', 'E']:
            player1.move_east()
        elif action_input in ['w', 'W']:
            player1.move_west()
        elif action_input in['a', 'A']:
            player1.attack()
        elif action_input in['i', 'I']:
            player1.print_inventory()
        elif action_input in ['h', 'H']:
            player1.heal()
        elif action_input in ['q', 'Q']:
            sys.exit()
        else:
            print("Invalid action")


def get_player_command():
    return input("To traverse the game and see what wonders it holds you may issue these commands \n "
                 "'n' to go North, \n "
                 "'s' to go South, \n "
                 "'e' to go East \n "
                 "'w' to go West \n "
                 "'i' to look in your inventory \n "
                 "'q' to enter oblivion \n "
                 "'h' to heal \n "
                 "'a' to attack \n "
                 " Make your choice and seal your fate:")


play()

# Redundant assignment comments
# Declare all the rooms
# room = {
# 'outside':  Room("Outside Cave Entrance",
# "North of you, the cave mount beckons"),

# 'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

# 'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

# 'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

# 'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']e
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']
