#dealer manages the game.
#initiate deck, player, shuffle / deal cards and evaluate hand strength for each player
#also be able to display table information

from param import *
from deck import Card 
from deck import Deck
from player import Player
from evaluator import Evaluator

class Dealer:

    def __init__(self, numPlayer, numPuppet=0, smallB=0):
        self.deck = Deck()
        self.propCards = []
        self.nextPropCard = 0
        self.community = []
        self.pot = 0
        self.smallB = smallB 
        self.winner = []
        self.players = []
        self.puppets = [] 
        self.button = 0
        for i in xrange(numPlayer): 
            newPlayer = Player(i, isPuppet=(i < numPuppet))
            self.players.append(newPlayer)
            if newPlayer.isPuppet:
                self.puppets.append(newPlayer)

    def addPropCards(self, cards):
        self.propCards.extend(cards)
    
    def startNewHand(self): 
        self.community = []
        self.pot = 0
        self.winner = []
        self.button = (self.button + 1) % numPlayer
        self.deck.shuffle()

    def dealHandCards(self): 
        players = self.players
        puppets = self.puppets
        deck = self.deck 
        button = self.button

        #set up puppets
        for i in xrange(len(puppets)):
            puppets[i].receiveCard(propCards[nextPropCard])
            puppets[i].receiveCard(propCards[nextPropCard+1])
            nextPropCard = (nextPropCard + 2) % len(propCards)

        for i in range(NUM_CARD_POCKET):
            for j in range(len(players)):
                player = players[(button + j) % len(players)]
                if not player.isPuppet: 
                    player.receiveCard(deck.getNext())
    
    def dealCommunityCards(self, num = 1):
        #no need to burn. increase complexity
        if nextPropCard != 0: 
            self.community.extend(propCards[nextPropCard:])
        num -= len(community)
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
        ref = Evaluator()
        for player in self.players: 
            ref.updateCards(player.cards + self.community)
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
        self.dealCommunityCards(NUM_CARD_COMMUNITY)
      
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

