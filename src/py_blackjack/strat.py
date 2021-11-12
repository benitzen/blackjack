#stop-at-17
import hand

def stop_at_17(p_hand,opponent_up_card):
    return hand.total(p_hand) < 17
        

def stop_at_n(n):
    def main_func(p_hand,h_hand):
        return hand.total(p_hand)<n
    return main_func

def dealer_hand(p_hand,h_hand):
    checker = True
    
    if (hand.total(p_hand) == 12 and (hand.total(h_hand) <=6 or hand.total(h_hand) >=4)):
        checker = False
    if ((hand.total(p_hand) == 13 or hand.total(p_hand) == 14) and hand.total(h_hand) <=6):
        checker = False
    if (hand.total(p_hand) == 15 and hand.total(h_hand) <= 6):
        checker = False
    if (hand.total(p_hand)== 16 and hand.total(h_hand) <= 6):
        checker = False
    if (hand.total(p_hand)== 17 and hand.total(h_hand)<=10):
        checker = False
    if ((hand.total(p_hand) >= 18 and hand.total(p_hand) <= 21) and hand.total(h_hand) <= 10):
        checker = False
    if (hand.total(p_hand)<=11 and hand.total(p_hand)>=5):
        checker = True
    if checker == False:
        return False
    else:
        return True
# def stop_at_what(n):
#     if hand.total([opponent_up_card]) < n:
#         return True

# def stop_at_n(n):
#     if hand.total([opponent_up_card]) < n:
#         return stop_at_what
#     else:
#         return True

# def take_into(p_hand,h_hand):
#     if count of dealer is < 6; your hand stop at 13 