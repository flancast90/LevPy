# LevPy: A Python JSON level-loader
# for easier level abstraction 
# in text-based py games

# Copyright (c) Finn Lancaster 2021

# pos will refer to the player's position 
# in a "room." Pos will need to be updated at function
# calls to account for the room the
# player is in.

import json 
from tabulate import tabulate
from main import *

pos = "Command1"
inp = "text"
inventory = []

def mainLoop(input_):
    global inp
    imp = json.loads(globals()[pos])[input_]
    askUser = input(imp+'\n\n')
    #Always listen for help, and call the 
    #help function when entered
    if askUser == "help":
        print(help_())
        mainLoop(inp)
    #do the same for inventory as help
    elif askUser == "inventory":
        print(inventory_())
        mainLoop(inp)
    else:
        inp = imp
        callFunc_Update = pos+"_"
        globals()[callFunc_Update](askUser)

def inventory_():
    return "Your inventory contains: "+str(inventory)

def help_():
    l = [["Command Category","Command Syntax"]]
    commandTable = tabulate(l, headers=["Category", "Command Text"], tablefmt="orgtbl")
    return commandTable

# We will feed the default command to this
# as Command1. If the user enters
# Command2 or Command3, it will give the
# JSON text associated with them

# This is what is called for command1
# And will contain the input needed
# for the user to move-on.

# For example, if the user must enter
# "Command2" to win, do the following.
# Command2 could also be changed so-as
# to call a new function that also listens
def Command1_(update):
#IMP, Command1 must include _ after to
# make a distinction between the var name
    global pos, inventory
    if update != "Command2":
        pos = "Command1"
        mainLoop(update)
    else:
        print("You Won!")
        inventory.append("New Object")

mainLoop("Command1")
