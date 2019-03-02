from blackjack import Card, Deck, Player

def test_Card():

    card = Card(rank=7, suit="Hearts")
    assert isinstance(card, Card) is True
    assert card.rank == 7
    assert card.suit == "Hearts"

    return

def test_Deck():
    
    deck = Deck()
    assert isinstance(deck, Deck)
    assert deck.cards != None
    assert len(deck.cards) == 52

    return

def test_Shuffle():

    d = Deck()
    # store deck before shuffling for comparison
    cardsBeforeShuffle = str(d.cards)
    d.shuffle()
    
    assert str(d.cards) != cardsBeforeShuffle

    return


def test_DrawCard():

    d = Deck()
    d.shuffle()

    c = d.drawCard()

    assert isinstance(c, Card) == True
    assert c not in d.cards

    return


def test_Player():

    p1 = Player("Matt")
    p2 = Player("Penny")

    assert isinstance(p1, Player)
    assert p1.name == "Matt"

    assert isinstance(p1, Player)
    assert p2.name == "Penny"

    return


def test_SinglePlayerDrawCard():
        
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