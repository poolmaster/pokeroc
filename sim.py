# simulator class
# decouple game simulation from dealer
# potentially allow multi-dealer simulation to accelerate / multi-thread
from param import *
from dealer import Dealer

class Sim:
    def __init__(
        self, 
        numPlayer=2, numPuppet=1, 
        puppetHands=[], propCommunity=[]):
        self.numGame = 0
        self.dealer = Dealer(numPlayer, numPuppet)
        for hand in puppetHands:
            self.dealer.addPropCards(hand)
        self.dealer.addPropCards(propCommunity)

    def play(self):
        self.dealer.play()
        self.dealer.judge()
        self.numGame += 1

    def display(self):
        print "----round %d info----" % self.numGame
        self.dealer.displayCommunity()
        self.dealer.displayPlayers()    
        self.dealer.displayWinners()
        print "----round %d info----\n\n" % self.numGame
