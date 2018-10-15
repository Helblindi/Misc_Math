from random import shuffle

suits = ("Spades", "Hearts", "Clubs", "Diamonds")

class Card:
    def __init__(self, rank, suit):
        if rank not in range(1, 14):
            raise TypeError('Rank must be an integer between 1 and 13.')
        if suit not in suits:
            raise TypeError('Suit must be a string: "Spades", "Hearts", "Clubs", or "Diamonds".')
        # The quick check above makes sure the card being made actually exists in a standard deck of 52.
        # If so, the card is created successfully.
        self.rank = rank
        self.suit = suit

    def __str__(self):
        special_cards = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}
        rank_name = special_cards[self.rank] if self.rank in special_cards else self.rank
        return '%s of %s' % (rank_name, self.suit)

    def card_name(self):
        special_cards = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}
        rank_name = special_cards[self.rank] if self.rank in special_cards else self.rank
        return '%s of %s' % (rank_name, self.suit)

    def flip(self):
        """
        Reveals the requested card.
        """
        print(self.card_name())


class Deck:
    def __init__(self):
        """
        Resets the deck to ascending order, containing all 52 cards.
        """
        self.contents = [Card(rank, suit) for suit in suits for rank in range(1, 14)]
        # So that the bottom of the list is the top of the deck, i.e.
        # the Ace of Spades is drawn first by 'self.contents.pop()'.
        self.contents.reverse()

    def shuffle_deck(self):
        """
        Self-explanatory. Shuffles the deck.
        """
        # Python's pseudo-random generator is slightly patterned unless shuffled multiple times.
        for i in range(0, 3):
            shuffle(self.contents)

    def draw(self):
        """
        Draws a single card to a variable.
        Useful for replacing and discarding individual cards in a hand, such as replacing cards in poker.
        To do so: <hand>[<card to replace>] = cards.draw()
        Remember that the list for a hand starts from 0, not 1.
        """
        rand_card = self.contents.pop()
        return rand_card

    def draw_face_up(self):
        rand_card = self.contents.pop()
        rand_card.flip()
        return rand_card

    def draw_hand(self, size):
        """
        Draws a <size>-card hand from the deck.
        """
        return [self.draw() for i in range(0, size)]


"""
Useful functions that do not belong in either the Card class of the Deck class.
"""
def show_hand(hand):
    size = len(hand)
    for i in range(0, size):
        hand[i].flip()

def cardHelp():
    """
    Gives a set of instructions explaining the use of the 'cards.py' module.
    """
    print('\n' + '=' * 72)
    print('=' * 13 + " [brilliantlyInsane]'s Python Cards: Instructions " + '=' * 14)
    print('=' * 72 + '\n')

    print('—' * 16 + " The Cards " + '—' * 45)
    print('—' * 72)
    print('The "Card" object has two attributes:')
    print('rank - An integer between 1 and 13. (Ace = 1, Jack = 11, Queen = 12, King = 13.)')
    print('suit - A string value of either "Spades", "Hearts", "Clubs", or "Diamonds".')
    print('A specific card object can be made: "Card(<rank>,<suit>)".\n')

    print('—' * 16 + " Drawing Cards " + '—' * 41)
    print('—' * 72)
    print('"Draw" cards to a variable with "<var> = cards.draw()".')
    print('Use "cards.draw_face_up() to draw a card and print its value.')
    print('"Flip" a card (print its value) with "<var>.flip()".')
    print('Generate an entirely new random card using "cards.new_card()".')
    print('(Note that "new_card()" duplicates a card in the deck.)\n')

    print('—' * 16 + " Hands " + '—' * 49)
    print('—' * 72)
    print('To draw an entire hand with <size> many cards, use "cards.draw_hand(<size>)".')
    print('To show a hand, use "cards.show_hand(<hand>)."\n')

    print('—' * 16 + " Replacing Cards " + '—' * 39)
    print('—' * 72)
    print('You can replace individual cards in a hand using <hand>[card #] = cards.draw().')
    print('However, lists in Python start FROM 0, not 1!')
    print('"hand[1] = cards.draw()" will replace the SECOND card in your hand, not the first!\n')

    print('—' * 16 + " The Deck " + '—' * 46)
    print('—' * 72)
    print('The deck is stored to a list under the variable "cards.self.contents".')
    print('Shuffle using "shuffle_deck()". The deck is unshuffled by default.')
    print('Reset the deck completely using cards.new_deck().')
    print('\n' + '=' * 72 + '\n')

    # Typing cards.cardHelp() will help you use this module
