from random import shuffle

class Card():

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

    def __str__(self):

        return "{} of {}".format(self.rank, self.suit)

    def show(self):

        print( "{} of {}".format(self.rank, self.suit) )

        return 


class Deck():

    def __init__(self):

        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

        self.cards = [ Card(rank, suit) for rank in self.ranks for suit in self.suits ]

    def show(self):
        
        for card in self.cards:
            print(card) 

        return

    def shuffle(self):
        
        return shuffle(self.cards)


    def drawCard(self):
        
        return self.cards.pop()


class Player():

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        print( "{}'s hand:".format(self.name) )
        for card in self.hand:
            print("  " + str(card)