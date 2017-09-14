# record simulation results per hand
# calculate odds
# read and return odds results
# interact with DB

from __future__ import division
from datetime import date
from collections import defaultdict
from dealer import Dealer
from param import *
import utils

class dbNode:
    def __init__(self, winOdds=0.0, tieOdds=0.0, count=0):
        self.winOdds = winOdds
        self.tieOdds = tieOdds
        self.count = count
     
    def merge(self, other):
        #no merge if count base > 10x
        if (self.count > other.count * 20 or
            self.count < other.count / 20): 
            return None
        else:
            winSum0 = self.winOdds * self.count
            winSum1 = other.winOdds * other.count
            tieSum0 = self.tieOdds * self.count
            tieSum1 = other.tieOdds * other.count
            self.winOdds = (winSum0 + winSum1) / (self.count + other.count)
            self.tieOdds = (tieSum0 + tieSum1) / (self.count + other.count)
            self.count = self.count + other.count
            return self
    
    def psdisplay(self, prefix=""): 
        log = prefix
        log += ("{:1.6f}".format(self.winOdds) + ",\t")
        log += ("{:1.6f}".format(self.tieOdds) + ",\t")
        log += str(self.count) 
        return log

    def psdisplay_percent(self, prefix=""): 
        log = prefix
        log += (str(self.winOdds * 100) + "%, ")
        log += (str(self.tieOdds * 100) + "%, ")
        log += str(self.count) 
        return log


class Bookeeper:
    def __init__(self, dbName, dbg=False):
        self.cntPlayerWins = defaultdict(int) #allow direct access without creation
        self.cntPlayerTies = defaultdict(int)
        self.cntCard = defaultdict(int)
        self.dbName = dbName
        self.dbHash = {}
        self.dbg = dbg
 
    def recordGame(self, dealer, puppetOnly=True): 
        winners = dealer.winner
        puppets = dealer.puppets
        tie = (len(winners) > 1)
        for player in winners:
            if puppetOnly:
                if player not in puppets: continue
            if not tie:
                self.cntPlayerWins[player.id] += 1
            else: 
                self.cntPlayerTies[player.id] += 1

    def recordCard(self, dealer):
        for player in dealer.players:
            for card in player.cards:
                self.cntCard[card] += 1
        for card in dealer.community:
            self.cntCard[card] += 1

    def mergeNodes(self):
        if self.dbg: print "merging nodes..."
        for key in self.dbHash.keys():
            for node in self.dbHash[key]:
                if node.count == 0: continue
                for other in self.dbHash[key]:
                    if node is other: continue
                    if node.merge(other) != None:
                        other.count = 0 #clear merging node
    
    def overwriteDB(self):
        if self.dbg: print "overwriting DB..."
        dbFile = open(self.dbName, "w")
        dbFile.write(DB_HEADER)
        dbFile.write("\n\n")
        for key in self.dbHash.keys():
            for node in self.dbHash[key]:
                if node.count != 0:
                    dbFile.write(node.psdisplay(key + ", "))
                    dbFile.write("\n")
        dbFile.close()
    
    def appendDB(self, dealer, numSim):
        if self.dbg: print "writing (appending) DB..."
        dbFile = open(self.dbName, "a")
        dbFile.write("\n\n# new appended simulation data: " + str(date.today()))
        dbFile.write("\n")
        for player in dealer.puppets:
            hand = utils.getHandStr(player.cards)
            winOdds = self.cntPlayerWins[player.id] / numSim
            tieOdds = self.cntPlayerTies[player.id] / numSim
            node = dbNode(winOdds, tieOdds, numSim)
            dbFile.write(node.psdisplay(hand + ", "))
            dbFile.write("\n")
        dbFile.close()
        
    def readDB(self): 
        if self.dbg: print "reading DB..."
        dbFile = open(self.dbName, "r")
        for entry in dbFile:
            entry = entry.strip()
            if entry == "" or entry[0] == '#':
                continue
            key, winOdds, tieOdds, count = [x.strip() for x in entry.split(',')]
            newNode = dbNode(float(winOdds), float(tieOdds), int(count))
            if key not in self.dbHash:
                self.dbHash[key] = [newNode]
            else: 
                self.dbHash[key].append(newNode) 
        dbFile.close()
        self.mergeNodes()
        if self.dbg: 
            for key in self.dbHash.keys():
                for node in self.dbHash[key]:
                    print node.psdisplay_percent(key + ", ")

    def findDbNode(self, hand):
        #find node with max count
        if hand not in self.dbHash:
            return None
        resNode = self.dbHash[hand][0]
        for node in self.dbHash[hand]:
            if node.count > resNode.count:
                resNode = node
        return resNode
         
    def getHandOdds(self, hand): 
        cardList = utils.getCardList(hand)
        hand = utils.getHandStr(cardList)
        return self.findDbNode(hand).psdisplay_percent()
          
    def getPlayerOdds(self, pid, numSim): 
        winOdds = self.cntPlayerWins[pid] / numSim
        tieOdds = self.cntPlayerTies[pid] / numSim
        node = dbNode(winOdds, tieOdds, numSim)
        return node.psdisplay_percent()
         


