import random as rd
import time

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    
    def __repr__(self):
        return f"I am {self.name} and my current score is {self.score}.\n"


def ace_score():
        check = False
        while not check:
            score = int(input(f"You drew the {RNG_key} so choose 2 or 11. \n"))
            if score == 2 or score == 11:
                check = True
                return score


def draw():
    RNG_pair = rd.choice(list(cards.items()))
    RNG_key = RNG_pair[0]
    if RNG_key in ["Ace Of Clubs", "Ace Of Spades", "Ace Of Diamonds", "Ace Of Hearts"]:
        print(ace_score())
    else:
        print(RNG_key)
        print(RNG_pair[1])


active_players = []
print("WELCOME TO BLACK JACK!")
valid_count = False
while not valid_count:
    print("2-4 players\n")
    players = int(input("How many players are we dealing with?\n"))
    if players > 1 and players < 5:
        valid_count = True
        print("\n")


if players == 2:
    name_1 = input("First player name: ")
    player_1 = Player(name_1)
    active_players.append(player_1)
    name_2 = input("Second player name: ")
    player_2 = Player(name_2)
    active_players.append(player_2)
    print("\n")
    for player in active_players:
        print(player)
    time.sleep(2)
elif players == 3:
    name_1 = input("First player name: ")
    player_1 = Player(name_1)
    active_players.append(player_1)
    name_2 = input("Second player name: ")
    player_2 = Player(name_2)
    active_players.append(player_2)
    name_3 = input("Third player name: ")
    player_3 = Player(name_3)
    active_players.append(player_3)
    print("\n")
    for player in active_players:
        print(player)
    time.sleep(2)
elif players == 4:
    name_1 = input("First player name: ")
    player_1 = Player(name_1)
    active_players.append(player_1)
    name_2 = input("Second player name: ")
    player_2 = Player(name_2)
    active_players.append(player_2)
    name_3 = input("Third player name: ")
    player_3 = Player(name_3)
    active_players.append(player_3)
    name_4 = input("Fourth player name: ")
    player_4 = Player(name_4)
    active_players.append(player_4)
    print("\n")
    for player in active_players:
        print(player, "\n")
    time.sleep(2)

# Dictionary of all values
cards = {"Two Of Hearts": 2,
    	   "Three Of Hearts": 3,
         "Four Of Hearts": 4,
         "Five Of Hearts": 5,
         "Six Of Hearts": 6,
         "Seven Of Hearts": 7,
         "Eight Of Hearts": 8,
         "Nine Of Hearts": 9,
         "Ten Of Hearts": 10,
         "Jack Of Hearts": 11,
         "Queen Of Hearts": 11,
         "King Of Hearts": 11,
         "Ace Of Hearts": None,

         "Two Of Diamonds": 2,
         "Three Of Diamonds": 3,
         "Four Of Diamonds": 4,
         "Five Of Diamonds": 5,
         "Six Of Diamonds": 6,
         "Seven Of Diamonds": 7,
         "Eight Of Diamonds": 8,
         "Nine Of Diamonds": 9,
         "Ten Of Diamonds": 10,
         "Jack Of Diamonds": 11,
         "Queen Of Diamonds": 11,
         "King Of Diamonds": 11,
         "Ace Of Diamonds": None,

         "Two Of Spades": 2,
         "Three Of Spades": 3,
         "Four Of Spades": 4,
         "Five Of Spades": 5,
         "Six Of Spades": 6,
         "Seven Of Spades": 7,
         "Eight Of Spades": 8,
         "Nine Of Spades": 9,
         "Ten Of Spades": 10,
         "Jack Of Spades": 11,
         "Queen Of Spades": 11,
         "King Of Spades": 11,
         "Ace Of Spades": None,

        "Two Of Clubs": 2,
         "Three Of Clubs": 3,
         "Four Of Clubs": 4,
         "Five Of Clubs": 5,
         "Six Of Clubs": 6,
         "Seven Of Clubs": 7,
         "Eight Of Clubs": 8,
         "Nine Of Clubs": 9,
         "Ten Of Clubs": 10,
         "Jack Of Clubs": 11,
         "Queen Of Clubs": 11,
         "King Of Clubs": 11,
         "Ace Of Clubs": None,
}
