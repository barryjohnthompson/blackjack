"""
Tests for the blackjack.py models.
"""

from blackjack import Card, Deck, Player

def test_Card():
    """
    Test that a card object is created correctly.
    """

    card = Card(rank=7, suit="Hearts")
    assert isinstance(card, Card) is True
    assert card.rank == 7
    assert card.suit == "Hearts"

    return

def test_Deck():
    """
    Test that a deck object is created correctly.
    """

    deck = Deck()
    assert isinstance(deck, Deck)
    assert deck.cards != None
    assert len(deck.cards) == 52

    return

def test_Shuffle():
    """
    Test that a deck of cards is shuffled correctly.
    """

    d = Deck()
    # store deck before shuffling for comparison
    cardsBeforeShuffle = str(d.cards)
    d.shuffle()
    
    assert str(d.cards) != cardsBeforeShuffle

    return


def test_DrawCard():
    """
    Test that a card is drawn from a deck correctly.
    """

    d = Deck()
    d.shuffle()

    c = d.drawCard()

    assert isinstance(c, Card) == True
    assert c not in d.cards

    return


def test_Player():
    """
    Test that player objects are created correctly.
    """

    p1 = Player("Matt")
    p2 = Player("Penny")

    assert isinstance(p1, Player)
    assert p1.name == "Matt"

    assert isinstance(p1, Player)
    assert p2.name == "Penny"

    return


def test_SinglePlayerDrawCard():
    """
    Test that a single player can draw a card from a deck to their hand. Ensure the card is present in the player's hand
    but not present in the deck after being drawn.
    """

    d = Deck()
    d.shuffle()
    p1 = Player("Matt")

    for i in range(2):
        p1.draw(d)

    assert p1.hand != None
    assert len(p1.hand) > 0
    
    for card in p1.hand:
        assert card not in d.cards

    return


def test_MultiplePlayerDrawCard():
    """
    Test that multiple players can draw cards from a deck to their hand. Ensure the card is present in the player's hand
    but not present in the deck after being drawn or in the other player's hand.
    """

    d = Deck()
    d.shuffle()
    p1 = Player("Matt")
    p2 = Player("Sarah")

    for i in range(2):
        p1.draw(d)
        p2.draw(d)

    assert len(p1.hand) > 0
    assert len(p2.hand) > 0

    for card in p1.hand:
        assert card not in d.cards
        assert card not in p2.hand

    for card in p2.hand:
        assert card not in d.cards
        assert card not in p1.hand

    return