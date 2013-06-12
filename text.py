####################################################
#### Copy/Paste this code and then run it off   ####
#### the command prompt(double click the file)  ####
####################################################
# north, south, east, west
#               |14|
# -------------
# |10 |11 |:::| |12| |15|
# ------------- 
# | 7 | 8 | 9 | |13| 
# ------------- 
# | 5 | 2 | 3 | 
# ------------- 
# | 6 | 1 | 4 | 
# ------------- 
class character:
    def __init__(self):
        self.pos = 0
        self.inventory = []
        self.health = 100
    def damage(self, num):
        self.health -= num
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
armory = [0,6,2,0] #room 5
closet = [5,0,1,0] #room 6
locked_door = [0,0,8,0] #room 7
second_floor = [0,2,9,7] #room 8
dead_end = [0,3,0,8] #room 9
attic = [0,7,11,0] #room 10
window = [0,0,12,11] #room 11
ground = [14,13,15,0] #room 12
grass1 = [0,12,0,0] #room 13
grass2 = [0,0,0,12] #room 14
grass3 = [12,0,0,0] #room 15
room_map = [null,hall,staircase,wine_cellar,kitchen,armory,closet, #first floor
            locked_door,second_floor,dead_end,attic,window, #second floor 
            ground,grass1,grass2,grass3 #outside
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
    10:'Attic',
    11:'You are by the window, would you like to jump?',
    12:'You fell to the ground and lie there for a while....',
    13:'Just some grass'
}
room_items = {
    1: 'shattered_glass',
    2:'dust',
    3:'vodka',
    4:'Dungeon',
    5:'key',
    6:'skull',
    7:'bottle',
    8:'boar',
    9:'Corona',
    10:'feather',
    11: None,
    12: None
}
def init():  
    room = location(1)
    room.setDescription(room_descriptions[1])
    room.addItem(room_items[1])   
    print '''
    ...A dark guise envelops you...
    Hit enter to continue
    '''
    x = raw_input('> ')
    print '''
    ...You wake up in the same brothel you fell asleep in.
    ...
    The trough is beside you, your ammo is missing and so is your pistol.
    ...
    Hit enter to continue
    '''
    x = raw_input('> ')
    print '''
    Your mind is baffled, withering away as you lay there...
    '''
    print '''
    You regain conciousness...
    Some time has passed
    Hit enter to continue
    '''
    print '''
    commands:
    help for help,
    inventory for inventory,
    look for looking,
    take for taking,
    exit for exiting
    north, south, east, and west for moving
    for more type in 'help'
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
        north
    elif index == 12:
        player.damage(10)
        print "Current health: ",player.health
    else:
        print "can't go any further"
def look(args):
    print player.pos.description
    print "Items available here: ",str(player.pos.inventory).strip('[]')
def inventory(args): 
    print "You are carrying:"
    print str(player.inventory).strip('[]')
def take(args):
    try:
        if len(player.inventory) > 10:
            print "Not enough space, delete some items to keep it under 10"
        elif args[0] in player.pos.inventory:
            player.inventory += [args[0]]
            player.pos.deleteItem(args[0])
            print "You have taken the",args[0]
        elif len(args) == 0:
            print "Take what?"
        else:
            print "There are none of these here"
    except:
        print "Take what?"
def delete(args):
    if args[0] in player.inventory:
        del player.inventory[player.inventory.index(item)]
    elif len(args) == 0:
        "Delete what?"
    else:
        print "This item is not in your inventory"
def health(args):
    print "Your health is: "
    print player.health
def Exit(args):
    global go
    go = False
def gamehelp(args):
    print '''commands:
    help for help,
    inventory for inventory,
    look for looking,
    take for taking,
    exit for exiting
    north, south, east, and west for moving
    health for checking your health'''
def north(args):
    global index
    try:
        room = location(room_map[index][0])
        room.setDescription(room_descriptions[room_map[index][0]])
        room.addItem(room_items[room_map[index][0]])
        move(room_map[index][0])
        index = room_map[index][0]
    except:
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
        inspect()
commands = {
    'help': gamehelp,
    'inventory': inventory,
    'look': look,
    'take': take,
    'delete': delete,
    'exit': Exit,
    'health': health,
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
