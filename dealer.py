#dealer manages the game.
#initiate deck, player, shuffle / deal cards and evaluate hand strength for each player
#also be able to display table information

from param import *
from card import Card 
from deck import Deck
from player import Player
from evaluator import Evaluator

class Dealer:
    #instance variable:
    #deck
    #community[]
    #pot
    #smallB
    #winner
    #players
    #button
    def __init__(self, numOfPlayer, smallB=0):
        self.deck = Deck()
        self.community = []
        self.pot = 0
        self.smallB = smallB 
        self.winner = []
        self.players = []
        self.button = 0
        for i in xrange(numOfPlayer):
            newPlayer = Player(i)
            self.players.append(newPlayer)
    
    def startNewHand(self): 
        self.community = []
        self.pot = 0
        self.winner = []
        self.button += 1
        self.deck.shuffle()
      
    def dealHandCards(self): 
        players = self.players
        deck = self.deck 
        button = self.button
        for i in xrange(len(players)):
            players[(button + i) % len(players)].receiveCard(deck.getNext())
        for i in xrange(len(players)):
            players[(button + i) % len(players)].receiveCard(deck.getNext())
    
    def dealCommunityCards(self, num = 1):
        #no need to burn. increase complexity
        #self.deck.getNext()
        for i in xrange(num):
            self.community.append(self.deck.getNext())
    
    def comparePlayers(self, A, B):
        if(A.handRank > B.handRank):
            return 1
        if(A.handRank < B.handRank):
            return -1
        if(A.handVal > B.handVal):
            return 1
        if(A.handVal < B.handVal):
            return -1
        return 0
    
    def judge(self): 
        for player in self.players: 
            ref = Evaluator(player.cards + self.community)
            ref.evaluate()
            player.evaluate(ref)
        winner = [self.players[0]]
        for i in xrange(1, len(self.players)):
            if(self.comparePlayers(winner[0], self.players[i]) < 0):
                winner = [self.players[i]]
            elif(self.comparePlayers(winner[0], self.players[i]) == 0): 
                winner.append(self.players[i])
        self.winner = winner 
        return winner
      
    def displayPlayer(self, pos):
        print "----player %d pocket cards----" % pos
        self.players[pos].displayHand()
    
    def displayWinner(self):
        print "----winner(s):----"
        for player in self.winner:
            player.displayHand()
    
    def displayCommunity(self):
        print "----community cards: flop, river, turn----"
        for card in self.community:
            card.display()

