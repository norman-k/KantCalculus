####################################################
#### Copy/Paste this code and then run it off   ####
#### the command prompt(double click the file)  ####
####################################################
# north, south, east, west
# ------------- 
# | 5 | 2 | 3 | 
# ------------- 
# | 6 | 1 | 4 | 
# ------------- 
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
null = [0,0,0,0]
hall = [2,0,4,6]
staircase = [0,1,3,5]
wine_cellar = [0,4,0,2]
kitchen = [3,0,0,1]
armory = [0,6,2,0]
closet = [5,0,1,0]
room_map = [null,hall,staircase,wine_cellar,kitchen,armory,closet] 
room_descriptions = {
    1:'You are by the hall',
    2:'You are by the staircase',
    3:'You are by the wine_cellar',
    4:'You are by the kitchen',
    5:'You are by the armory',
    6:'You are by the closet'
}
room_items = {
    1:'shattered_glass',
    2:'dust',
    3:'bottle',
    4:'Dungeon',
    5:'vodka',
    6:'dust'
}
def init():  
    room = location(1)
    room.setDescription(room_descriptions[1])
    room.addItem(room_items[1])   
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
    take for taking,
    exit for exiting
    north, south, east, and west for moving
    '''
    move(1)
index = 1
def move(site):
    player.pos = locations[site]
def look(args):
    print player.pos.description
    print player.pos.inventory
def inventory(args): 
    print "You are carrying:"
    print player.inventory
def take(args):
    if args[0] in player.pos.inventory:
        player.inventory += [args[0]]
        player.pos.deleteItem(args[0])
        print "You have taken",args[0]
    elif len(args) == 0:
        print "Take what?"
    else:
        print "There are none of these here"
def Exit(args):
    global go
    go = False
def gamehelp(args):
    print commands.keys()
def north(args):
    global index
    try:
        room = location(room_map[index][0])
        room.setDescription(room_descriptions[room_map[index][0]])
        room.addItem(room_items[room_map[index][0]])
        move(room_map[index][0])
        index = room_map[index][0]
    except:
        print "can't go any further"
def south(args):
    global index
    try: 
        room = location(room_map[index][1])
        room.setDescription(room_descriptions[room_map[index][1]])
        room.addItem(room_items[room_map[index][1]])
        move(room_map[index][1])
        index = room_map[index][1]
    except:
        print "can't go any further"
def east(args):
    global index
    try: 
        room = location(room_map[index][2])
        room.setDescription(room_descriptions[room_map[index][2]])
        room.addItem(room_items[room_map[index][2]])
        move(room_map[index][2])
        index = room_map[index][2]
    except:
        print "can't go any further"
def west(args):
    global index
    try: 
        room = location(room_map[index][3])
        room.setDescription(room_descriptions[room_map[index][3]])
        room.addItem(room_items[room_map[index][3]])
        move(room_map[index][3])
        index = room_map[index][3]
    except:
        print "can't go any further"
commands = {
    'help': gamehelp,
    'inventory': inventory,
    'look': look,
    'take': take,
    'exit': Exit,
    'north': north,
    'n': north,
    'south': south,
    's': south,
    'west': west,
    'w': west,
    'east': east,
    'e': east
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
