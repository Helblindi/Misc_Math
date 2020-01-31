"""
Work with Bro. Bessey.
"""

from deck_of_cards import *
from scipy.special import comb


def get_winning_set(v):
    """
    Function designed to return the values of a set that would allow you to win a round.
    This way the only use provided input for main is r and v.
    :param v: number of winning values
    :return: set of winning card numbers, values from 1 to 13
    """
    winning_set = []
    for i in range(1, v + 1):
        winning_set.append(i)

    return winning_set

def calc_probability_of_winning_hand(deck, winning_set, r):
    """
    Function to calculate the dependent probability of winning the next hand given the deck and the winning set.
    :param deck: Current state of the deck.  Not always of size 52.
    :param winning_set: Set of cards that are designated as "winning cards".
    :param r: number of cards dealt at a time
    :return: the probability out of 1.0 of winning this given hand
    """
    num_remaining_cards = deck.get_size()
    num_winning_cards = 0
    for card in deck.contents:
        # print(card)
        if card.rank in winning_set:
            num_winning_cards += 1
            # print('Found a winning card')

    # Way to calculate round win percentage per Dr. Bessey.
    probability_of_win = 1 - (comb(num_remaining_cards - num_winning_cards, r) / comb(num_remaining_cards, r))

    return probability_of_win

def play_round(r, v):
    """
    Function that plays through a whole round.  A round consists of dealing hand after hand until there is
    not enough cards remaining in the deck to deal out an addition hand.  The total hand count in a round
    is simply calculated as 52 / r
    :param r: number of cards dealt per hand
    :param v: number of cards in the winning set
    :return:
    """
    winning_set = get_winning_set(v)

    # start with a shuffled new deck
    deck = Deck()
    deck.shuffle_deck()
    win_count = 0
    hand_count = 52 // r
    # print('hand_count: ', hand_count)
    prob = 0

    # main loop of the round
    while deck.get_size() >= r:

        # e probabiFirst calculate the probability of winning the given hand so that we can get an
        # averaglity of winning each hand.
        probability_of_winning_hand = calc_probability_of_winning_hand(deck, winning_set, r)
        # print('prob of winning hand: ', probability_of_winning_hand)
        prob += probability_of_winning_hand

        hand = deck.draw_hand(r)

        # determine if we won the hand
        for card in hand:
            if card.rank in winning_set:
                win_count += 1
                print('rank: ', card.rank)
                break

    # if we won the round, return 1, else return 0
    win_val = 0
    if win_count >= 0.5 * hand_count:
        win_val = 1

    return win_val, float(prob / hand_count)

def main():
    # 'r' denotes the number of cards dealt at a time 1 <= r <= 52
    # 'v' denotes the number of distinct winning card values. 1 <= v <= 13
    # 'num_rounds' is the predefined number of rounds our game will consist of
    r = 2  # 1 <= r <= 52
    v = 5  # 1 <= v <= 13
    num_rounds = 10

    round_win_count = 0
    total_hand_win_percentage = 0
    for i in range(num_rounds):
        win_val, hand_win_percentage = play_round(r, v)
        round_win_count += win_val
        total_hand_win_percentage += hand_win_percentage

    avg_hand_win_percentage = float(total_hand_win_percentage / num_rounds)
    print('Total hand win percentage: ', avg_hand_win_percentage)

    round_win_percentage = float(round_win_count / num_rounds)
    print('round_win_count: ', round_win_count, 'num_rounds: ', num_rounds, 'win percentage: ', round_win_percentage)

    # create a table that stores the data nicely
    # create_probability_table(6, 6, 10)


def create_probability_table(r, v, num_rounds):
    """
    Display a table of the probabilities given r and v
    :param r: Number of cards dealt at a time.
    :param v: Number of distinct winning card values
    :param num_rounds: Number of rounds.
    :return: Nothing.  Prints out table of values.
    """
    print("r\tv\tavg hand win percentage\tavg round win percentage")
    print('---\t---\t----------------------- \t------------------------')

    for i in range(2, r + 1):
        for j in range(2, v + 1):
            round_win_count = 0
            total_hand_win_percentage = 0
            for it in range(num_rounds):
                win_val, hand_win_percentage = play_round(i, j)
                round_win_count += win_val
                total_hand_win_percentage += hand_win_percentage

            avg_hand_win_percentage = float(total_hand_win_percentage / num_rounds)
            round_win_percentage = float(round_win_count / num_rounds)
            print(i, '\t', j, '\t', avg_hand_win_percentage, '\t', round_win_percentage)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
