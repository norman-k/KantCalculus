class character:
    def __init__(self):
        self.pos = 0
        self.inventory = []
        self.area = 0
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
        Commands()
    raw_input("Press Enter: ")
    
def init():
    room = location(0)
    room.setDescription("You are in a brothel.")
    room.addItem("wine bottle")
    
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
    commands: help for help, inventory for inventory, look for looking, exit for exiting
    '''
    move(0)
def move(site):
    player.pos = locations[site]
def look():
    print player.pos.description    
def inventory(): 
    print "You are carrying:"
    print player.inventory
def Exit():
    global go
    go = False
def gamehelp():
    print "Commands: help, inventory, look, exit"
def Commands():
    print '\n'
    read_commands = raw_input("> ").split()
    if read_commands == []:
        input= ""
    else:
        input = read_commands[0]
    if input =="exit":
        global go
        go = False
    elif input =="look": 
        look()
    elif input =="help": 
        gamehelp()
    elif input =="inventory":
        inventory()
    elif input =="":
        print "Type a command"
    else:
        print "Some share thoughts"


main()







