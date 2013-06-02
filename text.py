class character:
    def __init__(self):
        self.inventory=[]
class location:
    def __init__(self, pos):
        self.pos = pos
        self.description = '[]'
        self.exits = {}
        self.inventory=[]
        locations[pos] = self
    def setDescription(self,description): 
        self.description=description 
    def addExit(self, name, item):
        self.exits[name]=item
    def addItem(self, item):
        self.inventory+=[item]
    def deleteItem(self, item):
        del self.inventory[self.inventory.index(item)]

locations = {}
p = character
go = True

def main():
    global go
    init()
    while go:
        commands()
        #if "x" in p.inventory:
        #    go = False
    raw_input("Press Enter: ")
def init():
    n = location(0)
    n.setDescription("You are in a brothel.")
    n.addExit("wine cellar",1)
    n.addItem("wine bottle")
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
    print 'commands: help for help, inventory for inventory, the rest are a mirage'
    x = raw_input('> ')
def commands():
    print '\n'
    read_commands = raw_input('> ').split()
    if read == []:
        input=''
    else:
        cmd = read[0]
    if input=="exit":
        global go
        go = False
    elif input=="help": 
        gamehelp()
    elif input=="inventory":
        inventory()
    elif input=="":
        print "Type a command"
    else:
        print "Some share thoughts"
def gamehelp(): 
    print "Commands you know: help inventory exit"
def inventory(): 
    print "You are carrying:"
    print p1.inventory
main()
