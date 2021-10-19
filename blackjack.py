from random import randint

# initialise cards by value in dictionary and lists

list2 = ["Two of hearts","Two of diamonds" ,"Two of spades", "Two of clubs"]
list3 = ["Three of hearts", "Three of diamonds", "Three of spades", "Three of clubs"]
list4 = ["Four of hearts", "Four of diamonds", "Four of spades", "Four of clubs"]
list5 = ["Five of hearts", "Five of diamonds", "Five of spades", "Five of clubs"]
list6 = ["Six of hearts", "Six of diamonds", "Six of spades", "Six of clubs"]
list7 = ["Seven of hearts", "Seven of diamonds", "Seven of spades", "Seven of clubs"]
list8 = ["Eight of hearts", "Eight of diamonds", "Eight of spades", "Eight of clubs"]
list9 = ["Nine of hearts", "Nine of diamonds", "Nine of spades", "Nine of clubs"]
list10 = ["Ten of hearts", "Ten of diamonds", "Ten of spades", "Ten of clubs"]
list_royals = ["Jack of hearts", "Jack of diamonds", "Jack of spades", "Jack of clubs",
              "King of hearts", "King of diamonds", "King of spades", "King of clubs",
              "Queen of hearts", "Queen of diamonds", "Queen of spades", "Queen of clubs"]
list_aces = ["Ace of hearts", "Ace of diamonds", "Ace of spades", "Ace of clubs"]

available_cards = {2: list2,
                   3: list3,
                   4: list4,
                   5: list5,
                   6: list6,
                   7: list7,
                   8: list8,
                   9: list9,
                   10: list10,
                   11: list_royals,
                   1: list_aces}

def draw_card():
    num = randint(1, 12)
    return num


print(draw_card())