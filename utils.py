#util functions
from param import *

def getHandIdx(cards):
    idx = -1
    big = cards[1]
    small = cards[0]
    if cards[0].rank > cards[1].rank:
        big = cards[0]
        small = cards[1]
    if cards[0].color == cards[1].color:
        idx = (big.rank - 1) * NUM_RANK + (small.rank - 1)
    else:
        idx = (small.rank - 1) * NUM_RANK + (big.rank - 1)
        
