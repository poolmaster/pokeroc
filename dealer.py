#dealer manages the game.
#initiate deck, player, shuffle / deal cards and evaluate hand strength for each player
#also be able to display table information

from param import *
from deck import Card 
from deck import Deck
from player import Player
from evaluator import Evaluator

class Dealer:

    def __init__(self, numPlayer, numPuppet=0):
        self.ref = Evaluator() #referee
        #self.pot = 0
        #self.smallB = smallB 
        self.winner = []
        self.players = []
        self.puppets = [] 
        self.button = 0
        for i in xrange(numPlayer): 
            newPlayer = Player(i, isPuppet=(i < numPuppet))
            self.players.append(newPlayer)
            if newPlayer.isPuppet:
                self.puppets.append(newPlayer)
        self.deck = Deck()
        self.deck.setNumCardToUse(
            NUM_CARD_POCKET * len(self.players) + NUM_CARD_COMMUNITY 
        )
        self.propCards = []
        self.nextPropCard = 0
        self.community = []

    def addPropCards(self, cards):
    #format [puppet_1's card, puppet_2's card, prop_community card]
        self.propCards.extend(cards)
        self.deck.addHidCards(cards)
    
    def startNewHand(self): 
        self.community = []
        self.winner = []
        self.nextPropCard = 0
        self.deck.shuffle()
        for player in self.players:
            player.reset()
        #self.pot = 0
        self.button = (self.button + 1) % len(self.players)

    def dealHandCards(self): 
        players = self.players
        puppets = self.puppets
        deck = self.deck 
        button = self.button
        #set up puppets
        for i in xrange(len(puppets)):
            puppets[i].receiveCard(self.propCards[self.nextPropCard])
            puppets[i].receiveCard(self.propCards[self.nextPropCard+1])
            self.nextPropCard = self.nextPropCard + 2
        for i in range(NUM_CARD_POCKET):
            for j in range(len(players)):
                player = players[(button + j) % len(players)]
                if not player.isPuppet: 
                    player.receiveCard(deck.getNext())
    
    def dealCommunityCards(self, num = 1):
        #no need to burn. increase complexity
        if self.nextPropCard != len(self.propCards): 
            self.community.extend(self.propCards[self.nextPropCard:])
        num -= len(self.community)
        for i in xrange(num):
            self.community.append(self.deck.getNext())
     
    def judge(self): 
        for player in self.players: 
            player.evaluate(self.ref, self.community) 
        winner = [self.players[0]]
        for i in xrange(1, len(self.players)):
            if winner[0].handVal < self.players[i].handVal:
                winner = [self.players[i]]
            elif winner[0].handVal == self.players[i].handVal:
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
        self.dealCommunityCards(NUM_CARD_COMMUNITY)
      
    def displayPlayers(self):
        for player in self.players:
            print "----player %d pocket cards----" % player.id
            print player.psdisplay()
    
    def displayWinners(self):
        print "----winner(s):----"
        for player in self.winner:
            log = "player %d: " % player.id
            log += player.psdisplay()
            print log
    
    def displayCommunity(self):
        print "----community cards: flops, river, turn----"
        log = ""
        for card in self.community:
            log += card.psdisplay()
        print log

