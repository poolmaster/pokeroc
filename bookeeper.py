# record simulation results per hand
# calculate odds
# read and return odds results
# interact with DB

from __future__ import division
from utils import *
from collections import defaultdict

class Bookeeper:
    def __init__(self, dbName):
        self.cntAll = 0
        #self.cntHandWins = [0 for x in xrange(NUM_HAND)] 
        #self.cntHandTies = [0 for x in xrange(NUM_HAND)]
        self.cntHandWins = {}
        self.cntHandTies = defaultdict(int)
        self.cntHandTies = {}
        self.cntHandWins = defaultdict(int)
        self.dbWinOdds = {}
        self.dbTieOdds = {}
        self.dbCnts = {}
        self.dbName = dbName

    def update(self, players, winners): 
        cntAll += 1
        tie = False 
        for player in winner:
            hand = getHandStr(player.cards)
            if not tie:
                cntHandWins[hand] += 1
            else:
                cntHandTies[hand] += 1

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
            dbWinOdds[elements[0]] = elements[1]
            dbTieOdds[elements[0]] = elements[2]
            dbCnts[elements[0]] = elements[3]
        dbFile.close()
        
    def getWinOdd(self, hand): 
        if dbCnt[hand] > cntHandWins[hand]:
            return dbWinOdds[hand]
        else:
            return cntHandWins[hand] / cntAll 
    
    def getTieOdd(self, hand): 
        return cntHandTies[hand] / cntAll 

    def getCnt(self, hand):
        return dbCnt[hand]

