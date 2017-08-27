from param import *
from deck import Card
from evaluator import Evaluator

class Player:
    #instance variable
    #cards[]
    #pos
    #bet
    #handRank
    #handVal
    #isPuppet
    #cntWin
    #cntTie
    def __init__(self, pos=-1,isPuppet=False):
        self.cards = []
        self.pos = pos
        self.bet = 0
        self.handRank = 0
        self.handVal = 0
        self.isPuppet = isPuppet;
        self.cntWin = 0
        self.cntTie = 0
    
    def setPos(self, pos):
        self.pos = pos
    
    def resetHist(self):
        self.cntWin = 0
        self.cntTie = 0

    def receiveCard(self, card): 
        self.cards.append(card) 
     
    def evaluate(self, ref):
        self.handRank = ref.handRank
        self.handVal = ref.value
    
    def displayHand(self, prefix=""):
        for card in self.cards:
            card.display()
        print "%s %s val=%d val(binary)=%s" %(prefix, HAND_RANK_LIST[self.handRank], self.handVal, bin(self.handVal))
   
