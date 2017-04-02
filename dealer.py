#dealer manages the game.
#initiate deck, player, shuffle / deal cards and evaluate hand strength for each player
#also be able to display table information

from param import *
from deck import Card 
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
    #numPuppet
    #button
    def __init__(self, numPlayer, numPuppet= 0, smallB=0):
        self.deck = Deck()
        self.propCards = []
        self.community = []
        self.pot = 0
        self.smallB = smallB 
        self.winner = []
        self.players = []
        self.button = 0
        self.numPuppet = numPuppet 
        for i in xrange(numPlayer): 
            newPlayer = Player(i, i < numPuppet)
            self.players.append(newPlayer)

    def initPropCards(self, cards):
        for i in xrange(len(cards)):
            propCards.append(cards[i])
    
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
            player = players[(button + i) % len(players)]
            if not player.isPuppet: 
                player.receiveCard(deck.getNext())
        j = 0
        for i in xrange(len(players)):
            players[(button + i) % len(players)].receiveCard(deck.getNext())
            if not player.isPuppet: 
                player.receiveCard(deck.getNext())
            else:
                player.receiveCard(propCards[j])
                player.receiveCard(propCards[j+1])
                j += 2
    
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

    def getResult(self, player):
        result = LOOSE
        for winPlayer in winner:
            if player is winPlayer:
                result = WIN if len(winner) == 1 else TIE
        return result

    def play(self):
        self.startNewHand()
        self.dealHandCards()
        self.dealCommunityCards(5)
      
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

