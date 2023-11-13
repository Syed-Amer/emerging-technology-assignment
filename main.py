from webexteamssdk import WebexTeamsAPI, ApiError
import os

# Function to test the connection
def test_Connection(api):
    try:
        api.people.me()
        return True
    except ApiError:
        return False

# function to list rooms
def listRooms(api):
    rooms = api.rooms.list()
    print("\nRooms List:")
    i = 1
    for room in rooms[:5]:
        print(f"\n{i}. Room Name: {room.title}\n   Room Id: {room.id}\n   Date Created: {room.created}\n   Date of Last Activity: {room.lastActivity}")
        i = i + 1
    

# clear terminal
os.system("clear")

# prompt access token from user
access_token = input("enter access token: ")

# create WebexTeamsApi instance
api = WebexTeamsAPI(access_token=access_token)

while True:
    choice = input("\nOption 0: Test Connection\nOption 1: Display my info\nOption 2: List Rooms\nOption 3: Create room\nOption 4: Send Message\n\nEnter your option: ")

    if choice == '0':
        if test_Connection(api):
            print("\nConnection success")

        else:
            print("\nConnection failed\nPlease enter valid access token if you want to use other option")

    elif choice == '1':

        if test_Connection(api):
            me = api.people.me()
            email_list = ', '.join(me.emails)

            print("\nDisplay Name: " + me.displayName +
            "\nNickname    : " + me.nickName +
            "\nEmails      : " + email_list)

        else:
            print("Please enter valid access token first")


    elif choice == '2':

        if test_Connection(api) == 1:
           listRooms(api)

        else:
            print("\nPlease enter valid access token first")

    elif choice == '3':
        if test_Connection(api):
            roomName = input("\nPlease enter new room name: ")

            # store list of rooms in rooms
            rooms = api.rooms.list()

            # iterate rooms to check if the room name already exists
            for room in rooms:
                if roomName == room.title:
                    print("exist")
                    break

            # if not exists, then create the room
            else:
                try:
                    api.rooms.create(roomName)
                    print("room create")
                except ApiError:
                    print("Error creating room!")
                except TypeError:
                    print("invalid value")
        else:
            print("\nPlease enter valid access token first")

    elif choice == '4':
        if test_Connection(api) == 1:
            listRooms(api)

            # create array to store roomsId
            roomsId = []
            
            for room in api.rooms.list()[:5]:

                # append the room's id in the array
                roomsId.append(room.id)

            # room to send message to
            roomToSend = int(input("\nPlease enter which number room to send message to: "))

            # message to send
            message = input("Enter message you want to send: ")

            if api.messages.create(roomsId[roomToSend-1], text=message):
                print("\nGG! Message sent!!!!!")

            else:
                print("Error sending message")
            
        else:
            print("\nPlease enter valid access token first")

    else:
        print("invalid input")

    menu = input("\nGo to the main menu? (y/n): ")
    if menu == 'y':
        os.system("clear")
    elif menu == 'n':
        print("Exiting the program.")
        break
    else:
        print("invalid input")
        break