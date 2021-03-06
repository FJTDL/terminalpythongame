# Importing libraries.
import random as rd
import time

# Defining player class
class Player:

    done = False
    score = 0

    def __init__(self, name):
        self.name = name
        self.score = 0

    
    def __repr__(self):
        return f"I am {self.name} and my current score is {self.score}.\n"

# Defininf methods for players to draw.
def draw_1():
    print(f"Ready {player_1.name}")
    time.sleep(1)
    global RNG_key
    RNG_pair = rd.choice(list(cards.items()))
    RNG_key = RNG_pair[0]
    if RNG_key in ["Ace Of Clubs", "Ace Of Spades", "Ace Of Diamonds", "Ace Of Hearts"]:
        check = False
        global score
        while not check:
            score = int(input(f"You drew the {RNG_key} so choose 2 or 11. \n"))
            if score == 2 or score == 11:
                check = True
                player_1.score += score
        print(player_1)
    else:
        print(RNG_key)
        player_1.score += RNG_pair[1]
        print(player_1)
    if player_1.score < 21:
        finished = None
        while finished not in ["hit", "stand"]:
            finished = input("Hit or Stand?").lower()
        if finished.lower() == "stand":
            return None
        else:
            draw_1()
    if player_1.score == 21:
        return None
    if player_1.score > 21:
        player_1.score = 0
        print(f"BUST")
        return None


def draw_2():
    print(f"Ready {player_2.name}")
    time.sleep(1)
    global RNG_key
    RNG_pair = rd.choice(list(cards.items()))
    RNG_key = RNG_pair[0]
    if RNG_key in ["Ace Of Clubs", "Ace Of Spades", "Ace Of Diamonds", "Ace Of Hearts"]:
        check = False
        global score
        while not check:
            score = int(input(f"You drew the {RNG_key} so choose 2 or 11. \n"))
            if score == 2 or score == 11:
                check = True
                player_2.score += score
    else:
        print(RNG_key)
        player_2.score += RNG_pair[1]
        print(player_2)
    if player_2.score < 21:
        finished = None
        while finished not in ["hit", "stand"]:
            finished = input("Hit or Stand?").lower()
        if finished.lower() == "stand":
            return None
        else:
            draw_2()
    if player_2.score == 21:
        return None
    if player_2.score > 21:
        player_2.score = 0
        print(f"BUST")
        return None


def draw_3():
    print(f"Ready {player_3.name}")
    time.sleep(1)
    global RNG_key
    RNG_pair = rd.choice(list(cards.items()))
    RNG_key = RNG_pair[0]
    cards.pop(RNG_key)
    if RNG_key in ["Ace Of Clubs", "Ace Of Spades", "Ace Of Diamonds", "Ace Of Hearts"]:
        check = False
        global score
        while not check:
            score = int(input(f"You drew the {RNG_key} so choose 2 or 11. \n"))
            if score == 2 or score == 11:
                check = True
                player_3.score += score
    else:
        print(RNG_key)
        player_3.score += RNG_pair[1]
        print(player_3)
    if player_3.score < 21:
        finished = None
        while finished not in ["hit", "stand"]:
            finished = input("Hit or Stand?").lower()
        if finished.lower() == "stand":
            return None
        else:
            draw_3()
    if player_3.score == 21:
        return None
    if player_3.score > 21:
        player_3.score = 0
        print(f"BUST")
        return None


def draw_4():
    print(f"Ready {player_4.name}")
    time.sleep(1)
    global RNG_key
    RNG_pair = rd.choice(list(cards.items()))
    RNG_key = RNG_pair[0]
    cards.pop(RNG_key)
    if RNG_key in ["Ace Of Clubs", "Ace Of Spades", "Ace Of Diamonds", "Ace Of Hearts"]:
        check = False
        global score
        while not check:
            score = int(input(f"You drew the {RNG_key} so choose 2 or 11. \n"))
            if score == 2 or score == 11:
                check = True
                player_4.score += score
    else:
        print(RNG_key)
        player_4.score += RNG_pair[1]
        print(player_4)
    if player_4.score < 21:
        finished = None
        while finished not in ["hit", "stand"]:
            finished = input("Hit or Stand?").lower()
        if finished.lower() == "stand":
            return None
        else:
            draw_4()
    if player_4.score == 21:
        return None
    if player_4.score > 21:
        player_4.score = 0
        print(f"BUST")
        return None
            

# Starting the game
active_players = []
print("WELCOME TO BLACK JACK!")


# Function used to start game
def starter():
    global players
    valid_count = False
    while not valid_count:
        print("2-4 players\n")
        try:
            players = int(input("How many players are we dealing with?\n"))
            
        except:
            starter()
        if 5 > players > 1:
            valid_count = True
    
# Starts game
starter()

# Start of game logic
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

if players == 2:
    
    draw_1()
    
    draw_2()

    if player_1.score > player_2.score:
        print(f"{player_1.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
    elif player_2.score > player_1.score:
        print(f"{player_2.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
    else:
        print("We have a tie...")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")

elif players == 3:

    draw_1()

    draw_2()

    draw_3()

    if player_1.score > player_2.score and player_1.score > player_3.score:
        print(f"{player_1.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
    elif player_2.score > player_1.score and player_2.score > player_3.score:
        print(f"{player_2.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
    elif player_3.score > player_2.score and player_3.score > player_1.score:
        print(f"{player_3.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
    else:
        print("We have a tie...")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")

else:
    draw_1()

    draw_2()

    draw_3()

    draw_4()

    if player_1.score > player_2.score and player_1.score > player_3.score and player_1.score > player_4.score:
        print(f"{player_1.name} wins!\n")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
        print(f"{player_4.name} : {player_4.score}\n")
    elif player_2.score > player_1.score and player_2.score > player_3.score and player_2.score > player_4.score:
        print(f"{player_2.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
        print(f"{player_4.name} : {player_4.score}\n")
    elif player_3.score > player_1.score and player_3.score > player_2.score and player_3.score > player_4.score:
        print(f"{player_3.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
        print(f"{player_4.name} : {player_4.score}\n")
    elif player_4.score > player_1.score and player_4.score > player_2.score and player_4.score > player_3.score:
        print(f"{player_4.name} wins!")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
        print(f"{player_4.name} : {player_4.score}\n")
    else:
        print("We have a tie...")
        print(f"{player_1.name} : {player_1.score}\n")
        print(f"{player_2.name} : {player_2.score}\n")
        print(f"{player_3.name} : {player_3.score}\n")
        print(f"{player_4.name} : {player_4.score}\n")
