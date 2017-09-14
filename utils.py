#util functions
from param import *
from deck import Card
import operator as op

def getHandStr(cards):
    color = ""
    ranks = ""
    if cards[0].color == cards[1].color:
        color = "s"
    else:
        color = "o"
    if cards[0] > cards[1]:
        ranks = RANK_LIST[cards[0].rank] + RANK_LIST[cards[1].rank]
    else:
        ranks = RANK_LIST[cards[1].rank] + RANK_LIST[cards[0].rank]
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

def getCardList(cardStr):
    expList = [x.strip() for x in cardStr.split(',')]
    cardList = []
    for exp in expList:
        if len(exp) == 3:
            if exp[2] == 's':
                exp = 's' + exp[0] + 's' + exp[1]
            elif exp[2] == 'o':
                exp = 's' + exp[0] + 'h' + exp[1]
            else:
                sys.exit("invalid str for cards: " + cardStr)
        i = 0
        while i < len(exp): 
            cardList.append(Card.fromStr(exp[i:i+2]))
            i += 2
    return cardList

def displayCards(cards, prefix=""):
    res = prefix
    for card in cards:
        res += card.psdisplay()
        res += " "
    return res

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: 
        return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer // denom

