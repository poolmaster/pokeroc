# record simulation results per hand
# calculate odds
# read and return odds results
# interact with DB

from __future__ import division
from collections import defaultdict
from dealer import Dealer
import utils

class Bookeeper:
    #instance variable:
    #cntPlayerWins, cntCard: for testing 
    #below are all dictionary of hand-str
    #cntHandWins, cntHandTies, dbWinOdss, dbTieOdds, dbCnts, dbName 
    def __init__(self, dbName):
        self.cntPlayerWins = defaultdict(int) #allow direct access without creation
        self.cntCard = defaultdict(int)
        self.cntHandWins = defaultdict(int) 
        self.cntHandTies = defaultdict(int)
        self.dbName = dbName
        self.dbWinOdds = {}
        self.dbTieOdds = {}
        self.dbCnts = {}
 
    def recordPlayer(self, dealer):
        winners = dealer.winner
        for player in winners:
            self.cntPlayerWins[player.id] += 1

    def recordCard(self, dealer):
        for player in dealer.players:
            for card in player.cards:
                self.cntCard[card] += 1
        for card in dealer.community:
            self.cntCard[card] += 1

    def recordHand(self, dealer): 
        winners = dealer.winner
        tie = (len(winners) > 1)
        for player in winners:
            hand = utils.getHandStr(player.cards)
            if not tie:
                self.cntHandWins[hand] += 1
            else:
                self.cntHandTies[hand] += 1
    
    def writeDB(self):
        dbFile = open(dbName, "w")
        #todo
        dbFile.close()
        
    def readDB(self): 
        dbFile = open(dbName, "w")
        for entry in dbFile:
            entry = entry.strip()
            if entry == "" or entry[0] == '#':
                continue
            elements = [x.strip() for x in entry.split(',')]
            self.dbWinOdds[elements[0]] = elements[1]
            self.dbTieOdds[elements[0]] = elements[2]
            self.dbCnts[elements[0]] = elements[3]
        dbFile.close()
        
    def getWinOdd(self, hand, cntAll=1): 
        if self.dbCnts[hand] > self.cntHandWins[hand]:
            return self.dbWinOdds[hand]
        else:
            return self.cntHandWins[hand] / cntAll 
    
    def getTieOdd(self, hand, cntAll=1): 
        return self.cntHandTies[hand] / cntAll 

    def getCnt(self, hand):
        return self.dbCnts[hand]

