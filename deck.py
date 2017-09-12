#52-card deck

import sys
import random
from param import *

class Card:
    #instance variable:
    #id, color, rank
    def __init__(self, color, rank, id=-1):
        self.color = color 
        self.rank = rank 
        self.id = id  #unique id

    @staticmethod 
    def fromStr(exp):
        if len(exp) != 2: 
            error = "invalid exp for card representaion: " + exp
            sys.exit(error)
        for color in COLOR_LIST:
            if exp[0] == color[0]:
                return Card(COLOR_DICT[color], RANK_DICT[exp[1].upper()])  

    @staticmethod 
    def fromId(id): 
        return Card(id / 13, id % 13)

    def compare(self, card):
        if self.rank > card.rank:
            return 1
        elif self.rank == card.rank:
            return 0
        else:
            return -1

    def psdisplay(self, prefix=""): 
        res = "" 
        res += COLOR_LIST[self.color]
        res += RANK_LIST[self.rank]
        res += " "
        return prefix+res


class Deck: 
    #instance variable
    #cards[] hidCards[], nextCard 
    def __init__(self):
        self.cards = []
        id = 0
        for i in xrange(NUM_COLOR):
            for j in xrange(NUM_RANK):
                newCard = Card(i, j, id)
                self.cards.append(newCard)
                id = id + 1
        self.nextCard = 0
        self.hidCards = []
        self.numCardToUse = NUM_CARD 
    
    def setNumCardToUse(self, num):
        self.numCardToUse = num
 
    def shuffle(self, startIdx=0):
        for i in xrange(startIdx, self.numCardToUse - 1): #last card does not swap
            randIdx = random.randrange(i, NUM_CARD) 
            self.cards[i], self.cards[randIdx] = self.cards[randIdx], self.cards[i] 
        self.nextCard = startIdx
    
    #just switch the card (target) with card of the target position in the deck
    def setCard(self, position, card):
        for i in xrange(NUM_CARD):
            if self.cards[i].color == card.color and self.cards[i].rank == card.rank:
                self.cards[i], self.cards[position] = self.cards[position], self.cards[i]      

    def removeCard(self, card):
        for i in xrange(NUM_CARD):
            if self.cards[i].color == card.color and self.cards[i].rank == card.rank:
                del self.cards[i]
    
    def addHidCards(self, cards): 
        self.hidCards.extend(cards)
     
    def getNext(self):
        while True:
            card = self.cards[self.nextCard]
            self.nextCard += 1 
            if card not in self.hidCards:
                break
        return card
        
  
