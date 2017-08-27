# contraint random generator for hands
# possible contraints:
#   number of cards: 5-card hands and 7-card hands
#   hand rank
#   fix some cards 
#   range of value

from param import *
import random

class HandGen:
    def __init__(self, numCards=5):
        self.numCards = numCards
        self.handRank = NOT_EVALUATE
        self.cards = [] 
        self.maxVal = 0
        self.minVal = 0

    def getRandomHand(self):
        hand = cards
        cards = [] #reset
        return hand
        
