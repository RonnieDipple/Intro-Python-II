import sys
from collections import OrderedDict
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
    print("Outside A Cave Entrance")
    world.parse_world_dsl()
    player1 = Player()
    wrapper = TextWrapper()
    wrapper.initial_indent = "* "
    while True:
        room = world.tile_at(player1.x, player1.y)
        print(room.intro_text())
        room.modify_player(player1)  # controls hp loss and death
        choose_action(room, player1)  # abstraction the core is below



def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
    if action:
        action()# short hand for if action!=None or if action is not None, then if function found it get's executed due to ()
    else:
        print("Invalid action")

# get_available_actions creates a dictionary of hotkey-action pairs.
def get_available_actions(room, player):# this prevents sill behaviors
    actions = OrderedDict() #dictionaries come disordered but not this one :)
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory") # Here I am just refering to the player.print_inventory function not executing it as we would if it was player.print_inventory()
        if isinstance(room, world.EnemyTile) and room.enemy.is_alive(): # This is not the first time I have used is instance but The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument)
            action_adder(actions, 'a', player.attack, "Attack")
        else:
            if world.tile_at(room.x, room.y - 1):
                action_adder(actions, 'n', player.move_north, "Go north")
            if world.tile_at(room.x, room.y + 1):
                action_adder(actions, 's', player.move_south, "Go south")
            if world.tile_at(room.x + 1, room.y):
                action_adder(actions, 'e', player.move_east, "Go east")
            if world.tile_at(room.x - 1, room.y):
                action_adder(actions, 'w', player.move_west, "Go west")
        if player.hp < 100:
            action_adder(actions, 'h', player.heal, "Heal")

        return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print(f"{hotkey}: {name}")


play()


# Redundant due to choose action
# def get_player_command():
# return input("To traverse the game and see what wonders it holds you may issue these commands \n "
# "'n' to go North, \n "
# "'s' to go South, \n "
# "'e' to go East \n "
# "'w' to go West \n "
# "'i' to look in your inventory \n "
# "'q' to enter oblivion \n "
# "'h' to heal \n "
# "'a' to attack \n "
# " Make your choice and seal your fate:")

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
