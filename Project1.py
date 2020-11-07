#  File: Project1.py
#  Description: An Adventure Game (part1) 
#  Student's Name:Chih-Yu Lin 
#  Student's UT EID:cl44344
#  Course Name: CS 303E 
#  Unique Number: 50191
#
#  Date Created: 2020/4/10
#  Date Last Modified: 2020/4/11

# the room in game
class Room:
    def __init__(self,_dict):
        self.name = _dict['name']
        self.north = _dict['north']
        self.east = _dict['east']
        self.south = _dict['south']
        self.west = _dict['west']
        self.up = _dict['up']
        self.down = _dict['down']
        self.contents = _dict['contents']
        
    # display the room and its around rooms
    def displayRoom(self):
        print("Room name:", self.name)
        if self.north:
            print("\tRoom to the north: ", self.north)
        if self.east:
            print("\tRoom to the east:  ", self.east)
        if self.south:
            print("\tRoom to the south: ", self.south)
        if self.west:
            print("\tRoom to the west:  ", self.west)
        if self.up:
            print("\tRoom above:        ", self.up)
        if self.down:
            print("\tRoom below:        ", self.down)
        if self.contents:
            contents = self.contents.split('/')
            content_tostring = "[ "
            print("\tRoom contents:        ", end = "")
            for content in contents:
                if content != "":
                    content_tostring += " ' "+  content.strip()+" ' "
            content_tostring += ']'
            print(content_tostring)
        else:
            print("\tRoom contents:         []")
        print()


def createRoom(roomData):
    return Room(roomData)


def look():
    global current
    print("You are currently in the %s." % current.name)
    print("contents of the room")
    if current.contents:
        index = 0
        contents = current.contents.split('/')
        index = len(contents)
        for content in contents:
            if content == "":
                index -=1
                continue
            print('\t'+content)
        if index <= 0:
            print('\tNone')
    else:
        print('\tNone')


def getRoom(name):
    global floorPlan
    for room in floorPlan:
        if room.name == name:
            return room


def move(direction):
    global current
    room = current.__getattribute__(direction)
    if room != 'None':
        curRoom = getRoom(room)
        print("You are now in the %s." % curRoom.name)
        return curRoom
    else:
        print("You can't move in that direction.")
        return current


def displayAllRooms():
    for room in floorPlan:
        room.displayRoom()

##########################################################################
###     All code below this is given to you.  DO NOT EDIT IT unless    ###
###     you need to adjust the indentation to match the indentation    ###
###     of the rest of your code.                                      ###
##########################################################################
        
def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable
    floorPlan = []
    with open('ProjectData.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('"', '')
            creat_room_dict={}
            room_info = line.rstrip("\n").split(',')
            content_info = ""
            if len(room_info) > 7:
                for i in range(7, len(room_info)):
                    content_info += room_info[i]+"/"
            creat_room_dict = {"name":room_info[0],"north":room_info[1],"east":room_info[2], "south":room_info[3], "west":room_info[4], "up":room_info[5], "down":room_info[6], "contents":content_info}
            floorPlan.append(createRoom(creat_room_dict))
        f.close()


def pickup(item_name):
    global current
    global inventory
    if current.contents:
        room_item_list = current.contents.split('/')
        _new_room_item_list = ""
        for item in room_item_list:
            if item_name == item:
                inventory.append(item_name)
                room_item_list.remove(item_name)
                for _item in room_item_list:
                    _new_room_item_list += _item+"/"
                current.contents = _new_room_item_list
                print("You now have the "+item)
                return
        print("That item is not in this room.")
    else:
        print("That item is not in this room.")


def drop(item_name):
    global current
    global inventory
    for item in inventory:
        if item == item_name:
            print("You have dropped the "+item)
            current.contents += item+"/"
            inventory.remove(item)
            return
    print("You dont have that item")


def listInventory():
    global inventory
    print("You are currently carring:")
    if len(inventory) <= 0:
        print("\tnothing.")
    else:
        for item in inventory:
            print("\t"+item)


def main():

    global current      # make the variable "current" a global variable
    global inventory
    inventory = []
    loadMap()
    
    displayAllRooms()
    current = floorPlan[0]
    look()
    # TEST CODE:  walk around the house
    command = ""
    ListofDirection =['north','east','south','west','up','down']
    while command != "exit":
        command = input("Enter a command:")
        if command == "help":
            print("look:    \tdisplay the name of the current room and its contents")
            print("north:   \tmove north")
            print("east:    \tmove east")
            print("south:   \tmove south")
            print("west:    \tmove west")
            print("up  :    \tmove up")
            print("down:    \tmove down")
            print("inventory:\tlist what items you're currently carrying")
            print("get <item>:\tpick up an item currently in the room")
            print("drop <item>:drop an item you're currently carrying")
            print("help:    \tprint this list")
            print("exit:    \tquit the game")
        elif command == "look":
            look()
        elif command in ListofDirection:
            current = move(command)
        elif command == "inventory":
            listInventory()
        elif command.startswith("get"):
            item_to_pick = command.split(" ")[1]
            pickup(item_to_pick)
        elif command.startswith("drop"):
            item_to_drop = command.split(" ")[1]
            drop(item_to_drop)





    


main()
