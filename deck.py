#52-card deck

import random
from param import *

class Card:
    #instance variable:
    #color
    #rank
    #id
    def __init__(self, color, rank, id):
        self.color = color 
        self.rank = rank 
        self.id = id  #unique id

    def compare(self, card):
        if self.rank > card.rank:
            return 1
        elif self.rank == card.rank:
            return 0
        else:
            return -1

    def display(self, prefix=""): 
        res = "" 
        res += COLOR_LIST[self.color]
        res += " "
        res += RANK_LIST[self.rank]
        print prefix+res
        return prefix+res


class Deck: 
    #instance variable
    #cards[]
    #nextCard  #pointer
    def __init__(self):
        self.cards = []
        id = 0
        for i in xrange(NUM_COLOR):
            for j in xrange(NUM_RANK):
                newCard = Card(i, j, id)
                self.cards.append(newCard)
                id = id + 1
        self.nextCard = 0
    
    def shuffle(self, startIdx=0):
        for i in xrange(startIdx, NUM_CARD - 1): #last card does not swap
            randIdx = random.randrange(i, NUM_CARD) 
            self.cards[i], self.cards[randIdx] = self.cards[randIdx], self.cards[i] 
        self.nextCard = startIdx
    
    #just switch the card (target) with card of the target position in the deck
    def setCard(position, card):
        for i in xrange(NUM_CARD):
            if self.cards[i].color == card.color and self.cards[i].rank == card.rank:
                self.cards[i], self.cards[position] = self.cards[position], self.cards[i]      

    def removeCard(card):
        for i in xrange(NUM_CARD):
            if self.cards[i].color == card.color and self.cards[i].rank == card.rank:
                del self.cards[i]
     
    def getNext(self):
        card = self.cards[self.nextCard]
        self.nextCard += 1 
        return card
        
  
