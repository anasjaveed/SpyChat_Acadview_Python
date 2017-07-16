from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from colour import Color
from datetime import datetime
import sys
from termcolor import colored, cprint

#importing colors from colors.py for output/messages.
from colors import prCyan, prRed, prYellow, prGreen, prLightPurple, prPurple , R , B , Black


#Status Message lists
STATUS_MESSAGES = ["'My name is Bond, James Bond'", "'Shaken, not stirred.'", "'Keeping the British end up, Sir'"]


question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)
if existing != 'Y' or existing != 'N':
    prRed('Wrong Input! Try Again')
    existing = raw_input(question)

#START Function to add status in SpyChat
def add_status():
    updated_status_message = None

    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    else:
        print 'The option you chose is not valid! Press either y or n.'
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'
    return updated_status_message
#END Function to add status in SpyChat

#START Function to add friend in SpyChat
def add_friend():
    new_friend = Spy('','',0,0.0)
    # Validation for not entering correct Name as input
    while True:
        new_friend.name = raw_input("Please add your friend's name: ")
        if new_friend.name.replace(" ", "").isalpha():
            break
        # Calling Color Red to print error message
        prRed("ERROR !!! Invalid Friend Name")
    # Validation for not entering correct Name as input
    while True:
        new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
        if new_friend.salutation.replace(".", "").isalpha():
            break
        # Calling Color Red to print error message
        prRed("ERROR !!! Invalid Friend Name")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    # Validation for not entering correct Age as input
    while True:
        new_friend.age = raw_input("Age? ")
        if  new_friend.age.replace("", "").isdigit():
            new_friend.age = int( new_friend.age)
            break
        # Calling Color Red to print error message
        prRed("ERROR !!! Age should be in NUMBERS")
    # Validation for not entering correct spy rating as input
    while True:
        new_friend.rating = raw_input("Spy rating? ")
        if new_friend.rating.replace(".", "").isdigit():
            new_friend.rating = float(new_friend.rating)
            break
        # Calling Color Red to print error message
        prRed("ERROR !!! Rating should be in Numbers and Precise")
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        prRed('Sorry! Invalid entry. We can\'t add spy with the details you provided')
    return len(friends)
#END Function to add friend in SpyChat

#START Function to select friend in SpyChat
def select_a_friend():
    item_number = 0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
        friend.age,friend.rating)
        item_number = item_number + 1
    friend_choice = raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position
#END Function to select friend in SpyChat

#START Function to send message in SpyChat
def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = "C:\Users\moham\Desktop\Secret\output.jpg"
    #Validation for not entering message
    while True:
        text = raw_input("What do you want to say? ")
        words = text.split()
        length=sum(len(word) for word in words)
        if text !=("") and length <=100:
            Steganography.encode(original_image, output_path, text)
            break
        prRed("ERROR !!! Either empty or 100 words exceeded")
    new_chat = ChatMessage(text,True)
    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"
#END Function to send message in SpyChat

#START Function to read message in SpyChat
def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    print secret_text
#END Function to read message in SpyChat

#START Function to read chat history in SpyChat
def read_chat_history():
    read_for = select_a_friend()
    print '\n'
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print'[%s] %s: %s' % (B+ chat.time.strftime("%d %B %Y"), R+ 'You said:', Black+ chat.message)
        else:
            print'[%s] %s said: %s' % (B+ chat.time.strftime("%d %B %Y"), R+ friends[read_for].name, Black+ chat.message)
#END Function to read chat history in SpyChat

#START Function to start SpyChat
def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"
        show_menu = True
        #To Display SpyChat Menu
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    prGreen('You have %d friends' % (number_of_friends))
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'
if existing.upper() == "Y":
    start_chat(spy)
else:
    spy = Spy('','',0,0.0)
    # Validation for spy name
    while True:
        spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
        if spy.name.replace(" ", "").isalpha():
            break
        # Calling Color Red to print error message
        prRed("ERROR !!! Invalid Name")
    if len(spy.name) > 0:
        # Validation for spy salutation
        while True:
            spy.salutation = raw_input("Should I call you Mr or Ms ?:")
            if spy.salutation.replace(".", "").isalpha():
                break
            # Calling Color Red to print error message
            prRed("ERROR !!! Invalid Salutation")
        # Validation for spy age
        while True:
            spy.age = raw_input("What is your age? ")
            if spy.age.replace("", "").isdigit():
                spy.age = int(spy.age)
                break
            # Calling Color Red to print error message
            prRed("ERROR !!! Age should be in NUMBERS")
        # Validation for spy rating
        while True:
            spy.rating = raw_input("What is your spy rating? ")
            if spy.rating.replace(".", "").isdigit():
                spy.rating = float(spy.rating)
                break
            prRed("ERROR !!! Rating should be in Numbers and Precise")
            # Condition to print spy_rating level
        if spy.rating > 0:
            if spy.rating >= 3.5 <= 5.0:
                prLightPurple("Expert Level")
            elif spy.rating  >=2.5 <=3.4:
                prPurple("Amateur Level")
            else:
                prYellow("Beginner Level")
        start_chat(spy)
    else:
        print 'Please add a valid spy name'
#END Function to start SpyChat


