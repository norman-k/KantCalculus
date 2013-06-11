####################################################
#### Copy/Paste this code and then run it off   ####
#### the command prompt(double click the file)  ####
####################################################
class character:
    def __init__(self):
        self.pos = 0
        self.inventory = []
class location:
    def __init__(self, num):
        self.num = num
        self.description = '[]'
        self.inventory = []
        locations[num] = self
    def setDescription(self, description): 
        self.description = description 
    def addItem(self, item):
        self.inventory += [item]
    def deleteItem(self, item):
        del self.inventory[self.inventory.index(item)]
locations = {}
player = character()
go = True
def main():
    global go
    init()
    while go:
            Commands(raw_input('> '))
    raw_input("Press Enter: ")
room_descriptions = {
    0:'You are in a brothel',
    1:'You are by the staircase',
    2:'You are by a strange labyrinth',
    3:'You are by the front door, its window is shattered'
}
room_items = {
    0:'wine bottle',
    1:'shattered glass'
    2:'dust',
    3:'shattered glass'
}
def init():  
    room = location(0)
    room.setDescription(room_descriptions[0])
    room.addItem(room_items[0])   
    print '''
    ...A dark guise envelops you. ..
    '''
    x = raw_input('> ')
    print '''
    ...You wake up in the same brothel you fell asleep in.
    ...
    The trough is beside you, your ammo is missing and so is your pistol.
    ...
    '''
    x = raw_input('> ')
    print '''
    Your mind is baffled, withering away as you lay there...
    '''
    print '''
    You regain conciousness...
    Some time has passed
    '''
    print '''
    commands:
    help for help,
    inventory for inventory,
    look for looking,
    exit for exiting
    north, south, east, and west for moving
    '''
    move(0)
room_number = 0
def move(site):
    player.pos = locations[site]
def look(args):
    print player.pos.description    
def inventory(args): 
    print "You are carrying:"
    print player.inventory
def Exit(args):
    global go
    go = False
def gamehelp(args):
    print "Commands: help, inventory, look, exit"
def north(args):
    room = location(1)
    room.setDescription(room_descriptions[1])
    room.addItem(room_items[1])
    move(1)
commands = {
    'help': gamehelp,
    'inventory': inventory,
    'look': look,
    'exit': Exit,
    'north': north,
    'south': south,
    'east': east,
    'west': west
}
def Commands(x):
    line = x.split()
    if line:
        if line[0] in commands:
            func = commands[line[0]]
            args = line[1:]
            func(args)
        else:
            print "I don't understand you"
    else:
        print "Some share thoughts"
main()
