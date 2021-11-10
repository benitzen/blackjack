# (def full-deck
#   (for [suit [:hearts :spades :diamonds :clubs]
        # rank (concat (range 2 11) [:J :Q :K :A])]
    # {:suit suit
    #  :rank rank}))

def full_deck():
    suit = ["hearts", "spades", "diamonds", "clubs"]
    for i in range(suit):
        suit[i].append("h0tdog")