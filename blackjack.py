"""
Basic OOP blackjack implementation
"""


from random import shuffle

class Card():
    """
    Class to represent a playing card.

    Args:
        rank(int or str) - value of the card
        suit(string)     - suit of the card    
    """

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

    def __str__(self):

        return "{} of {}".format(self.rank, self.suit)

    def show(self):
        """
        Print the card in a useful format.
        """

        print( "{} of {}".format(self.rank, self.suit) )

        return 


class Deck():
    """
    Class to represent a deck of playing cards.
    """

    def __init__(self):
        """
        Initialize and create a deck of cards.
        One card is created for each unique combination of suits and ranks.
        """

        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

        self.cards = [ Card(rank, suit) for rank in self.ranks for suit in self.suits ]

    def show(self):
        """
        Print the deck in a useful format.
        """
        
        for card in self.cards:
            print(card) 

        return

    def shuffle(self):
        """
        Shuffle the deck into a random order.
        """
        
        return shuffle(self.cards)


    def drawCard(self):
        """
        Remove a card from the deck.
        """
        
        return self.cards.pop()


class Player():
    """
    Represents a single player.
    """

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        """
        Draw a card from the specifdied deck and assign it to this player's hand.
        Args:
            deck - the deck object to draw a card from
        """
        self.hand.append(deck.drawCard())

    def showHand(self):
        """
        Print this player's hand in a useful format
        """
        print( "{}'s hand:".format(self.name) )
        for card in self.hand:
            print("  " + str(card))