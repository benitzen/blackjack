import random

official_deck = []


def full_deck():
    suit = []
    for i in range(4):
        if i == 0:
            suitName = "hearts"
        elif i == 1:
            suitName = "spades"
        elif i == 2:
            suitName = "diamonds"
        else:
            suitName = "clubs"
        print(suitName)
        for j in range(13):
            if j < 9:
                suit.append([suitName, str(j + 2)])
            elif j == 9:
                suit.append([suitName, "J"])
            elif j == 10:
                suit.append([suitName, "Q"])
            elif j == 11:
                suit.append([suitName, "K"])
            else:
                suit.append([suitName, "A"])
    return suit


def n_shuffled_decks(n):
    deck = full_deck()
    deck *= n
    random.shuffle(deck)
    return deck


def reset_deck():
    resetted_deck = n_shuffled_decks(4)
    return resetted_deck


official_deck = n_shuffled_decks(2)

# assumes you have an official deck
def deal():
    dealt_hand = official_deck.pop()
    print(dealt_hand)
    random.shuffle(official_deck)
    return dealt_hand


def new_hand():
    return [deal()]


def up_card(given_hand):
    return given_hand.pop()


def add_card(given_hand, card):
    given_hand.insert(0, card)


def total(given_hand):
    total_num = 0
    for i in range(len(given_hand)):
        if (
            given_hand[i][1] == "A"
            or given_hand[i][1] == "J"
            or given_hand[i][1] == "Q"
            or given_hand[i][1] == "K"
        ):
            total_num += 10
        else:
            total_num += int(given_hand[i][1])
    return total_num
