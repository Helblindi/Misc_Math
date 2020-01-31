from deck_of_cards import *

deck = Deck()
deck.shuffle_deck()

hand = deck.draw_hand(5)
for card in hand:
    print(card)