import threading, time
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
    0:'You are in a brothel'
}
room_items = {
    0:'wine bottle'
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
    '''
    move(0)
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
commands = {
    'help': gamehelp,
    'inventory': inventory,
    'look': look,
    'exit': Exit
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
