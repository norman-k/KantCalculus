####################################################
#### Copy/Paste this code and then run it off   ####
#### the command prompt(double click the file)  ####
####################################################
# north, south, east, west
# -------------
# |10 |   |   |
# ------------- 
# | 7 | 8 | 9 |
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
null = [0,0,0,0] #room 0, not possible to move further
hall = [2,0,4,6] #room 1
staircase = [8,1,3,5] #room 2
wine_cellar = [9,4,0,2] #room 3
kitchen = [3,0,0,1] #room 4
armory = [7,6,2,0] #room 5
closet = [5,0,1,0] #room 6
locked_door = [0,5,0,8] #room 7
second_floor = [0,2,9,7] #room 8
dead_end = [0,3,0,8] #room 9
attic = [7,0,0,0] #room 10
room_map = [null,hall,staircase,wine_cellar,kitchen,armory,closet,
            locked_door,second_floor,dead_end
            ] 
room_descriptions = {
    1:'You are by the hall',
    2:'You are by the staircase',
    3:'You are by the wine_cellar',
    4:'You are by the kitchen',
    5:'You are by the armory',
    6:'You are by the closet, a skull lays barren on the ground',
    7:'A locked door, in front of what looks like a small passageway',
    8:"You are on the second floor",
    9:'Dead end',
    10:'Attic'
}
room_items = {
    1:'shattered_glass',
    2:'dust',
    3:'bottle',
    4:'Dungeon',
    5:'key',
    6:'skull',
    7:'',
    8:'',
    9:'',
    10:''
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
def inspect():
    global room_map
    global locked_door
    if index == 7 and 'key' not in player.inventory:
        print "You need a key to get through here"
    elif index == 7 and 'key' in player.inventory:
        print "You opened the door using your key"
        locked_door[0] = 10
        room_map[8][0] = 10
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
        print "You have taken the",args[0]
    elif len(args) == 0:
        print "Take what?"
    else:
        print "There are none of these here"
def delete(args):
    if args[0] in player.inventory:
        del player.inventory[player.inventory.index(item)]
    elif len(args) == 0:
        "Delete what?"
    else:
        print "This item is not in your inventory"
def Exit(args):
    global go
    go = False
def gamehelp(args):
    for key in commands.keys():
        print key
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
        inspect()
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
        inspect()
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
        inspect()
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
        inspect()
commands = {
    'help': gamehelp,
    'inventory': inventory,
    'look': look,
    'take': take,
    'delete': delete,
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
