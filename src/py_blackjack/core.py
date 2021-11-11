import hand

# import add_card, deal, new_hand, up_card import hand


def stupid_strategy(p_hand, opponent_up_card):
    return hand.total([opponent_up_card]) > 5


def stop_at_17(hand, opponent_up_card):
    pass


def stop_at(n):
    pass


def play_hand(strategy, p_hand, opponent_up_card):
    if hand.total(p_hand) > 21:
        return p_hand
    elif strategy(p_hand, opponent_up_card):
        # recursion
        if strategy(p_hand, opponent_up_card):
            hand.add_card(p_hand, hand.deal())
            play_hand(strategy, p_hand, opponent_up_card)
        return p_hand
    else:
        return p_hand


def play_game(player_strategy, house_strategy):
    house_initial_hand = hand.new_hand()
    player_hand = play_hand(
        player_strategy, hand.new_hand(), hand.up_card(house_initial_hand)
    )

    if hand.total(player_hand) > 21:
        return 0
    else:
        house_hand = play_hand(
            house_strategy, house_initial_hand, hand.up_card(player_hand)
        )
        if hand.total(house_hand) > 21:
            return 1
        elif hand.total(play_hand) > hand.total(house_hand):
            return 1
        else:
            return 0


print(play_game(stupid_strategy, stupid_strategy))
