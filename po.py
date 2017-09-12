#!/usr/bin/env python2.7

from __future__ import division #force / to get float val

import random
from datetime import datetime
from param import *
from sim import Sim
from bookeeper import Bookeeper
import utils

dbName = "__stats.db"
logEnable = True
numSim = utils.ncr(52, 5)
numPlayer = 2
numPuppet = 2
puppetHands = [utils.getCardList("hA, hK"), utils.getCardList("sA, sK")]
propCommunity = utils.getCardList("dA, dK") 
propCommunity = []

#todo
#add command line support

#initialize
random.seed(datetime.now())
sim = Sim(numPlayer, numPuppet, puppetHands, propCommunity)
bookeeper = Bookeeper(dbName)

#simulate
for i in xrange(numSim):
    sim.play()
    bookeeper.recordHand(sim.dealer)
    if logEnable:
        sim.display()

#get odds
#for hand in puppetHands:
#    winOdd = bookeeper.getWinOdd(hand)
#    tieOdd = bookeeper.getTieOdd(hand)
#    print hand + " win: " + winOdd + " tie: " + tieOdd

#for i in xrange(len(dealer.players)):
#    dealer.displayPlayer(i)
#
#dealer.displayCommunity()
#
#dealer.displayWinner()

