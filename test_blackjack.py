from blackjack import Card, Deck, Player

# def test_Card():

#     card = Card(rank=7, suit="Hearts")
#     assert card.show() == "7 of Hearts"

#     return

# def test_Deck():
#     pass

# def test_Shuffle():

#     d = Deck()
#     tmp = d
#     d.shuffle()
    
#     assert d.show() != tmp.show()

#     return


# def test_Draw():

#     d = Deck()
#     d.shuffle()

#     c = d.draw()
#     print(c)

#     assert isinstance(c, Card) == True

d = Deck()
d.shuffle()
p1 = Player("Matt")
p2 = Player("Sarah")

for i in range(2):
    p1.draw(d)
    p2.draw(d)

p1.showHand()
p2.showHand()