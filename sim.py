#!/usr/bin/env python2.7

from __future__ import division

import random
from datetime import datetime
from param import *
from dealer import Dealer
from bookeeper import Bookeeper

dbName = "__stats.db"
numAllHand = 0
numPlayer = 2
numPuppet = 0
puppetHands = []
propCommunity = []
cntTotalHands = 0 #total hands

#todo
#add command line support

#initialize
random.seed(datetime.now())
dealer = Dealer(numPlayer, numPuppet)
for hand in puppetHands:
    dealer.addPropCards(hand)
dealer.addPropCards(propCommunity)
bookeeper = Bookeeper(dbName)

#simulate
for i in xrange(numAllHand):
    dealer.play()
    dealer.judge()
    bookeeper.update()

#get odds
for hand in puppetHands:
    winOdd = bookeeper.getWinOdd(hand)
    tieOdd = bookeeper.getTieOdd(hand)
    print hand + " win: " + winOdd + " tie: " + tieOdd

#for i in xrange(len(dealer.players)):
#    dealer.displayPlayer(i)
#
#dealer.displayCommunity()
#
#dealer.displayWinner()

