#evaluator takes in a hand and evaluate its strength
#cards are converted to pattern stored
#hand strength represented by __handRank and __value
from param import *
from deck import Card

MASK_RANK = [
    0b0000000000001,
    0b0000000000010,
    0b0000000000100,
    0b0000000001000,
    0b0000000010000,
    0b0000000100000,
    0b0000001000000,
    0b0000010000000,
    0b0000100000000,
    0b0001000000000,
    0b0010000000000,
    0b0100000000000,
    0b1000000000000
]

MASK_STRAIGHT = [
    0b1111100000000,
    0b0111110000000,
    0b0011111000000,
    0b0001111100000,
    0b0000111110000,
    0b0000011111000,
    0b0000001111100,
    0b0000000111110,
    0b0000000011111,
    0b1000000001111
]

class Evaluator:
    #instance variable
    #pattern  #per color
    #cntColor 
    #handRank
    #value
    #modeColor
    def __init__(self, cards):
        self.pattern = [0 for x in xrange(NUM_COLOR)]
        self.cntColor = [0 for x in xrange(NUM_COLOR)]
        self.handRank = HIGH_CARD 
        self.value = 0
        for card in cards:
            self.pattern[card.color] |= MASK_RANK[card.rank] 
            self.cntColor[card.color] += 1
        self.modeColor = self.cntColor.index(max(self.cntColor))
      
    def evalStraight(self, p = None):
        if p == None:
            p = self.pattern[0] | self.pattern[1] | self.pattern[2] | self.pattern[3]
        for i in xrange(len(MASK_STRAIGHT)):
            mask = MASK_STRAIGHT[i]
            if mask & p == mask: 
                self.handRank, self.value = STRAIGHT, (NUM_RANK - i)
                return True
        return False
          
    def evalFlush(self):
        cntRm = self.cntColor[self.modeColor] - 5
        if cntRm > 0:
            mask = 0b01
            p = self.pattern[self.modeColor]
            while cntRm > 0:
                if p & mask != 0:
                    p &= (~mask) 
                    cntRm -= 1
                mask = mask << 1
            self.handRank, self.value = FLUSH, p
            return True
        return False
    
    def evalQuads(self):
        quadPattern = self.pattern[0] & self.pattern[1] & self.pattern[2] & self.pattern[3]
        mergePattern = self.pattern[0] | self.pattern[1] | self.pattern[2] | self.pattern[3]
        if quadPattern != 0:
            self.handRank, self.value = QUADS, quadPattern 
            mergePattern = self.pattern[0] | self.pattern[1] | self.pattern[2] | self.pattern[3]
            for i in reversed(xrange(NUM_RANK)):
                if MASK_RANK[i] & mergePattern != 0 and MASK_RANK[i] != quadPattern:
                    self.value = self.value << NUM_RANK + MASK_RANK[i]   
                    break
        return (self.value > 0)
    
    def getMsb(self, val, num):
        p = 0b1000000000000
        res = 0
        while num > 0 and val > 0:
            if val & p:
                val &= ~p
                res |= p
                num -= 1 
            p = p >> 1
            #print "val=%s, num=%d, res=%s" %(bin(val), num, bin(res))
        return res
    
    
    def evalSetPair(self):
        setPattern = (
                        (self.pattern[0] & self.pattern[1] & self.pattern[2])
                      | (self.pattern[0] & self.pattern[1] & self.pattern[3]) 
                      | (self.pattern[0] & self.pattern[2] & self.pattern[3]) 
                      | (self.pattern[1] & self.pattern[2] & self.pattern[3]) 
                     )
        pairPattern = (
                         (self.pattern[0] & self.pattern[1]) | (self.pattern[2] & self.pattern[3])
                       | (self.pattern[0] & self.pattern[2]) | (self.pattern[1] & self.pattern[3])
                       | (self.pattern[0] & self.pattern[3]) | (self.pattern[1] & self.pattern[2])
                      )
        mergePattern = self.pattern[0] | self.pattern[1] | self.pattern[2] | self.pattern[3]
        #print "setPattern  " + bin(setPattern)
        #print "pairPattern " + bin(pairPattern)
        #print "merPattern  " + bin(mergePattern)
        if setPattern == 0: 
            if pairPattern == 0:
                self.handRank, self.value = HIGH_CARD, self.getMsb(mergePattern, NUM_CARD_HAND)
                return False
            elif ((pairPattern - 1) & pairPattern) == 0:
                self.handRank, self.value = ONE_PAIR, (pairPattern << NUM_RANK) | self.getMsb(mergePattern & ~pairPattern, 3)
            else:
                pairPattern = self.getMsb(pairPattern, 2)
                self.handRank, self.value = TWO_PAIR, (pairPattern << NUM_RANK) | self.getMsb(mergePattern & ~pairPattern, 1)
        elif (setPattern - 1) & setPattern == 0: 
            if pairPattern & ~setPattern == 0: 
                self.handRank, self.value = SET, (setPattern << NUM_RANK) | self.getMsb(mergePattern & ~setPattern, 2)
            else:
                self.handRank, self.value = FULL_HOUSE, (setPattern << NUM_RANK) | self.getMsb(pairPattern & ~setPattern, 1)
        else:
            setPattern = self.getMsb(setPattern, 1)
            self.handRank, self.value = FULL_HOUSE, (setPattern << NUM_RANK) | self.getMsb(pairPattern & ~setPattern, 1)
        #print "value= %s" %bin(self.value)
        return True
    
    
    def evaluate(self):
        flushVal, straightVal = self.evalFlush(), self.evalStraight(self.pattern[self.modeColor])
        if flushVal and straightVal:
            self.handRank, self.value = STRAIGHT_FLUSH, straightVal
            return STRAIGHT_FLUSH
        if self.evalQuads():
            return QUADS
        if self.evalSetPair():
            if self.handRank == FULL_HOUSE:
                return FULL_HOUSE 
        if self.evalStraight():
            return STRAIGHT
        
        return self.handRank
