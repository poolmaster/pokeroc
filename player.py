from param import *
from deck import Card
from evaluator import HandVal
from evaluator import Evaluator

class Player:
    #instance variable
    #id, cards[], bet, handVal, isPuppet, cntWin, cntTie
    def __init__(self, id=-1, isPuppet=False):
        self.id = id
        self.cards = []
        self.handVal = HandVal()
        self.isPuppet = isPuppet;
        #self.bet = 0
        #self.cntWin = 0
        #self.cntTie = 0

    def reset(self):
        self.cards = []
        self.handVal.reset()
        self.bet = 0
     
    #def resetHist(self):
    #    self.cntWin = 0
    #    self.cntTie = 0

    def receiveCard(self, card): 
        self.cards.append(card) 
     
    def evaluate(self, ref, community):
        self.handVal = ref.evaluate(self.cards + community)
    
    def psdisplay(self, prefix=""):
        info = prefix
        for card in self.cards:
            info += card.psdisplay()
            info += " "
        info += "hand evaluated: "
        info += self.handVal.psdisplay()
        return info 
