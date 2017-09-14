NUM_CARD = 52
NUM_RANK = 13
NUM_COLOR = 4
NUM_CARD_COMMUNITY = 5
NUM_CARD_POCKET = 2
NUM_CARD_SEEN = 7
NUM_CARD_HAND = 5
NUM_CARD_FLOP = 3

SPADE   = 0
HEART   = 1
CLUB    = 2
DIAMOND = 3
COLOR_LIST = ["spade", "heart", "club", "diamond"]
COLOR_DICT = {"spade" : 0, "heart" : 1, "club" : 2, "diamond" : 3}
RANK_LIST = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
RANK_DICT = {}
i = 0
for rank in RANK_LIST:
    RANK_DICT[rank] = i
    i += 1

NOT_EVALUATE   = 0
HIGH_CARD      = 1
ONE_PAIR       = 2
TWO_PAIR       = 3
SET            = 4
STRAIGHT       = 5
FLUSH          = 6
FULL_HOUSE     = 7
QUADS          = 8
STRAIGHT_FLUSH = 9
HAND_RANK_LIST = [
    "not_evaluated", 
    "high_card", 
    "one_pair", 
    "two_pair", 
    "set", 
    "straight", 
    "flush", 
    "full_house", 
    "quads", 
    "straight_flush"
]
HAND_RANK_DICT = {
    "not_evaluated" : 0,
    "high_card" : 1,
    "one_pair" : 2, 
    "two_pair" : 3, 
    "set" : 4, 
    "straight" : 5, 
    "flush" : 6, 
    "full_house" : 7, 
    "quads" : 8, 
    "straight_flush" : 9
}

LOSE = -1
TIE = 0
WIN = 1

NUM_HAND = 169 #78 suited + 13 pair + 78 off-suited

DB_HEADER = """# PokerOc DB
# statistical data accumulated through old simulation / sampling
# updates by new simulation / sampling is configurable

# format
# hand, winOdds, tieOdds, counts-winOdds-based-on
# AKs, 52.2, 0.0, 1000"""
