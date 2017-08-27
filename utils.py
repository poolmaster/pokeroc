#util functions
from param import *

def getHandStr(cards):
    color = ""
    ranks = ""
    if cards[0].color == cards[1].color:
        color = "s"
    else:
        color = "o"
    if cards[0] > cards[1]:
        ranks = RANK_LIST[cards[0]] + RANK_LIST[cards[1]]
    else:
        ranks = RANK_LIST[cards[1]] + RANK_LIST[cards[0]]
    return ranks + color

# hand index mapping
# AA  AKo AQo AJo ATo A9o A8o A7o ...
# AKs KK  KQo KJo KTo ...
# AQs KQs QQ  QJo QTo ...
# AJs KJs QJs JJ  JTo ...
# ...
def getHand2Idx(hand):
    idx = -1
    big, small = int(hand[0:1]), int(hand[1:2]) 
    if hand[-1:] == "o":
        idx = big.rank * NUM_RANK + small.rank
    else: #hand[-1:] == "s" 
        idx = small.rank * NUM_RANK + big.rank
    return idx

def getIdx2Hand(idx):
    hand = ""
    big = idx / NUM_RANK
    small = idx % NUM_RANK
    if big > small:
        hand = RANK_LIST[big] + RANK_LIST[small] + "o" 
    else:
        hand = RANK_LIST[small] + RANK_LIST[big] + "s"
    return hand 
