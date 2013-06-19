####################################################
#### Copy/Paste this code and then run it off   ####
#### the command prompt(double click the file)  ####
####################################################
# north, south, east, west
# = = = = = = = = = = = = = = =
#               |14| |16| |17| |18| :
# -------------           : :  |19| :
# |10 |11 |:::| |12| |15| : :  |20| :
# -------------           : :  |21| :
# | 7 | 8 | 9 | |13| |::| : :  |22| : |25|
# -------------                |23||24|
# | 5 | 2 | 3 | |::|
# ------------- 
# | 6 | 1 | 4 | 
# ------------- 
from random import randint
import math
class character:
    def __init__(self):
        self.pos = 0
        self.inventory = []
        self.health = 100
        self.mana = 100
    def damage(self, num):
        self.health -= num
    def addmana(self, num):
        if self.mana < 100:
            self.mama += num
        if self.mana > 100:
            self.mana = 100
    def subtractmana(self, num):
        if self.mana > 0:
            self.mana -= num
        if self.mana < 0:
            self.mana = 0
player = character()
class enemy_snake:
    def __init__(self):
        self.name = "snake"
        self.health = randint(1, math.ceil((player.health/10)))
    def damagetaken(self, num):
        self.health -= num
    def damagegiven(self):
        self.damagegiven = math.ceil(enemy.health/2)
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
snake = enemy_snake()
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
ground = [0,0,0,0] #room 12
grass1 = [12,0,0,0] #room 13
grass2 = [0,12,16,0] #room 14
grass3 = [16,0,0,12] #room 15
mail_box = [0,0,17,15] #room 16
sidewalk = [0,0,0,14] #room 17
open_door1 = [0,19,0,0] #room 18
hallway = [18,20,0,0] #room 19
hallway2 = [0,0,0,0] #room 20
hallway3 = [20,22,0,0] #room 21
hallway4 = [22,23,0,0] #room 22
hallway5 = [22,0,24,0] #room 23
second_section1 = [25,0,0,23] #room 24
second_section2 = [26,24,0,0] #room 25
room_map = [null,hall,staircase,wine_cellar,kitchen,armory,closet, #first floor
            locked_door,second_floor,dead_end,attic,window, #second floor 
            ground,grass1,grass2,grass3,mail_box,sidewalk, #outside
            open_door1,hallway,hallway2,hallway3,hallway4,hallway5, #second house layer 1 
            second_section1,second_section2 #second house layer 2
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
    11:'You are by the window, would you like to jump? To do so, go east',
    12:'You fell to the ground and lie there for a while....',
    13:'Just some grass',
    14:'Just some grass',
    15:'Just some grass',
    16:'A mailbox with an interesting parcel inside of it',
    17:'The lawn to a home, strangely quiet, go east when you have it',
    18:'Open door',
    19:'Hallway',
    20:'''
    You see a sword on the floor. You hear something in the background...',\nA snake approaches you, attack it!; ...and it killed you \ncongrats your journey has ended;
    sort of meaningless eh? \nWell hear you are in your afterlife fighting snakes, ...'
    ''',
    21:'''A snake approaches you, attack it!; ...and it killed you congrats your journey has ended;
    sort of meaningless eh? Well hear you are in your afterlife fighting snakes, ...'
    '''
}
room_items = {
    1: 'shattered_glass',
    2:None,
    3:'vodka',
    4:None,
    5:'key',
    6:'skull',
    7:'bottle',
    8:'boar',
    9:'Corona',
    10:'feather',
    11: None,
    12: None,
    13: None,
    14: None,
    15: None,
    16: 'letter',
    17:None,
    18:None,
    19:None,
    20:'sword',
    21:None
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
    '''
    print '''
    commands:
    help 'h' for help,
    inventory 'i' for inventory,
    look 'l' for looking,
    take 't' for taking,
    exit for exiting
    north 'n', south 's', east 'e', and west 'w' for moving
    for more type in 'help'
    '''
    move(1)
index = 1
first_letter =  '''
                Dear Sebastian,
                time is running out.
                I do not know how much
                longer I can hold out
        
                Please forgive me
                we must go.......
        
                ...
                The last few sentences are
                shrouded under ink blotches

                You put the letter back into
                your bag
                '''
def move(site):
    player.pos = locations[site]
def inspect():
    global index
    global room_map
    global locked_door
    global ground
    global sidewalk
    global first_letter
    if index == 7 and 'key' not in player.inventory:
        print "You need a key to get through here"
    elif index == 7 and 'key' in player.inventory:
        print "You opened the door using your key"
        locked_door[0] = 10
        room_map[8][0] = 10
        north('')
    elif index == 12:
        ground = [14,13,15,0]
        player.damage(10)
        print "Current health: "
        print player.health
        print "You stand up and go north"
        index += 2
        north('')
    elif index == 17 and 'letter' not in player.inventory:
        print "You forgot the letter!"
    elif index == 17 and 'letter' in player.inventory:
        sidewalk[2] = 18
        room_map[18][2] = 18
        print first_letter
        index += 2
        east('')
    elif index == 20 and 'sword' not in player.inventory:
        print "You can't move a snake is in your way! Grab the sword!"
    elif index == 20 and 'sword' in player.inventory:
        if snake.health == 0:
            hallway3 = [19,21,0,0]
            index += 2
            south('')
        else:
            print "Keep fighting till it's dead!"
            print "The snake's health: "
            print snake.health
    else:
        print "Can't go any further"
def look(args):
    print player.pos.description
    print "Items available here: ",str(player.pos.inventory).strip('[]')
    print "Exits available here: "
    exits = []
    for x in room_map[index]:
        if x != 0:
            if room_map[index][0] == x:
                exits.append('north')
            if room_map[index][1] == x:
                exits.append('south')
            if room_map[index][2] == x:
                exits.append('east')
            if room_map[index][3] == x:
                exits.append('west')
    if room_map[index] == [0,0,0,0]:
            print "The secrets out, move about"
    if len(exits) == 0:
            print "None"
    print str(exits).strip('[]')
    exits = []
def inventory(args): 
    print "You are carrying:"
    print str(player.inventory).strip('[]')
def quaff(args):
    try:
        if len(args) == 0:
            print str(player.inventory).strip('[]')
            print "Quaff what from your inventory?"
        elif args[0] in player.inventory:
            if args[0] == "vodka":
                print "Can't get drunk now"
            else:
                print "You can't quaff a",args[0]
        else:
            print "That item is not in your inventory"
    except:
        print "That item is not in your inventory"
def smite(args):
    try:
        if len(args) == 0:
            print str(room_descriptions[index]).strip('[]')
            print "Smite what in the room?"
        elif args[0] in room_descriptions[index]:
            if args[0] == "boar":
                print "You can't hurt a pig!"
            else: 
                print "You can't smite a",args[0]
        elif index == 20 and args[0]=='snake':
            if randint(1,4) == 2:
                player.damage(snake.damage)
                print player.health
                print "You missed!"
            else:
                snake.damagetaken(snake.health)
        else:
            print "What you wish to smite, is not here"
    except:
        print "What you wish to smite, is not here"
def read(args):
    if len(args) == 0:
        print str(player.inventory).strip('[]')
        print "Read what from your inventory?"
    elif args[0] in player.inventory:
        if args[0] == "letter":
            print first_letter
        else:
            print "You can't read that"
    else:
        print "That item is not in your inventory"
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
    try:
        if args[0] in player.inventory:
            del player.inventory[player.inventory.index(args[0])]
        elif len(args) == 0:
            "Delete what?"
        else:
            print "This item is not in your inventory"
    except:
        print "Delete what?"
def health(args):
    print "Your health is: "
    print player.health
def Exit(args):
    global go
    go = False
def gamehelp(args):
    print '''commands:
    help 'h' for help,
    inventory 'i' for inventory,
    read 'r' for reading,
    look 'l' for looking,
    quaff 'q' for drinking,
    smite 'sm' for smiting,
    take 't' for taking,
    delete 'del' for deleting,
    exit for exiting,
    north 'n', south 's', east 'e', and west 'w' for moving
    health for checking your health'''
def north(args):
    global index
    try:
        room = location(room_map[index][0])
        room.setDescription(room_descriptions[room_map[index][0]])
        room.addItem(room_items[room_map[index][0]])
        move(room_map[index][0])
        index = room_map[index][0]
        look('')
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
        look('')
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
        look('')
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
        look('')
    except:
        inspect()
commands = {
    'help':gamehelp,
    'h':gamehelp,
    'inventory':inventory,
    'i':inventory,
    'quaff':quaff,
    'q':quaff,
    'smite':smite,
    'sm':smite,
    'read':read,
    'r':read,
    'look':look,
    'l':look,
    'take':take,
    't':take,
    'delete':delete,
    'del':delete,
    'exit':Exit,
    'health':health,
    'north':north,
    'n':north,
    'south':south,
    's':south,
    'west':west,
    'w':west,
    'east':east,
    'e':east
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
