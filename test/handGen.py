# contraint random generator for hands
# possible contraints:
#   number of cards: 5-card hands and 7-card hands
#   hand rank
#   fix some cards 
#   range of value
import random
import sys
sys.path.append("..")

from param import *
from deck import Card

# hand_Rank     |   #value
# HIGH_CARD     |   5 MSBs from rank pattern
# ONE_PAIR      |   (pair-rank-bit << 13) + 3 MSBs from rank pattern
# TWO_PAIR      |   (pair-rank-pattern << 13) + MSB from rank pattern 
# SET           |   (triple-rank-bit << 13) + 2 MSBs from rank pattern 
# STRAIGHT      |   high-card rank in straight
# FLUSH         |   pattern value of flush color
# FULL_HOUSE    |   (triple-rank-bit << 13) + pair-rank-bit
# QUADS         |   (quad-rank-bit << 13) + MSB from rank pattern 
# STRAIGHT_FLUSH|   straight value

class HandGen:
    def __init__(self, numCards=5):
        self.numCards = numCards
        self.handRank = NOT_EVALUATE
        self.maxVal = 0
        self.minVal = 0

    def getRandomHand(self):
        if self.handRank == NOT_EVALUATE:
            return self.getHand()
        elif self.handRank == STRAIGHT_FLUSH:
            return self.getSf()
        elif self.handRank == QUADS:
            return self.getQuads()
        elif self.handRank == FULL_HOUSE:
            return self.getFullHouse()
        elif self.handRank == FLUSH:
            return self.getFlush()
        elif self.handRank == STRAIGHT:
            return self.getStraight()
        elif self.handRank == SET:
            return self.getSet()
        elif self.handRank == TWO_PAIR:
            return self.get2Pair()
        elif self.handRank == ONE_PAIR:
            return self.get1Pair()
        else:
            return getHighCard()

    def getHandFromIds(self, ids):
        hand = []
        for id in ids:
            hand.append(Card.fromId(id))
        return hand
        
    def getHand(self): 
        hand = []
        ids = random.sample(range(0, 52), self.numCards)
        return self.getHandFromIds(ids)

    def getSf(self):
        ids = [random.randint(0, 13 - 5) + random.randint(0, 4) * 13]
        for i in range(1, 5):
            ids.append(ids[0] + i)
        for i in xrange(len(ids), self.numCards):
            while True:
                id = random.randint(0, 52)
                if id not in ids:
                    break;
            ids.append(id)
        return self.getHandFromIds(ids)
        
    def getQuads(self):
        ids = []
        return self.getHandFromIds(ids)

    def getFullHouse(self):
        ids = []
        return self.getHandFromIds(ids)

    def getFlush(self):
        ids = []
        return self.getHandFromIds(ids)

    def getStraight(self):
        ids = []
        return self.getHandFromIds(ids)

    def getSet(self):
        ids = []
        return self.getHandFromIds(ids)

    def get2Pair(self):
        ids = []
        return self.getHandFromIds(ids)

    def get1Pair(self):
        ids = []
        return self.getHandFromIds(ids)

    def getHighCard(self):
        ids = []
        return self.getHandFromIds(ids)


