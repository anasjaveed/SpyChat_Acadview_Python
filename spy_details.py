from datetime import datetime
from colors import prCyan, prRed, prYellow, prGreen, prLightPurple, prPurple , B , Black

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = 'Hey! I am on SpyChat & Available'


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Anas', 'Mr.', 22, 4.7)

friend_one = Spy('Nasir', 'Mr.', 25, 4.9)
friend_two = Spy('Ayesha', 'Ms.', 21, 4.39)
friend_three = Spy('No', 'Dr.', 37, 4.95)
friends = [friend_one, friend_two, friend_three]


