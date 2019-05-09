###########################
##### CARD GAME: WAR! #####
###########################

# BASIC RULES:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS ]

        # [(s,r) for s in SUITE for r in RANKS ] is the same as:
        # mycards = []
        # for r in RANKS:
        #     for s in SUITE:
        #         mycards.append((s,r))

    # shuffle the cards
    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    # split the cards
    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])
        # return tuple of the cards

class Hand:

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    # add cards
    def add(self,added_cards):
        self.cards.extend(added_cards) #add it to the end

    # remove cards
    def remove_card(self):
        return self.cards.pop() #remove the last item

class Player:

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    # return true if player still have cards left
    def still_has_cards(self):

        return len(self.hand.cards) != 0


# start game
print("Welcome to War, let's begin...")

# Create New Deck
d = Deck()
d.shuffle() # shuffle the cards

# split cards in half
half1,half2 = d.split_in_half()

# Create Both Players
comp = Player("computer",Hand(half1))
name = raw_input("What is your name? ")
user = Player(name,Hand(half2))

# initialize Round Count
total_rounds = 0
war_count = 0

# Let's play
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(comp.name+" count: "+str(len(comp.hand.cards)))
    print("Both players play a card!")
    print('\n')

    # Cards on Table represented by list
    table_cards = []

    # Play cards
    c_card = comp.play_card()
    p_card = user.play_card()

    # Add to table_cards
    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for War!
    if c_card[1] == p_card[1]:
        war_count +=1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:
        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
