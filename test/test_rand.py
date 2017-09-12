#!/usr/bin/env python2.7

from __future__ import division #force / to get float val

import sys
sys.path.append("..")

import random
from datetime import datetime
from param import *
from sim import Sim
from bookeeper import Bookeeper
import utils

#init
random.seed(datetime.now())
sim = Sim(numPlayer=2, numPuppet=0)
bookeeper = Bookeeper("test_dummy.db")

#simulate
#numSim = utils.ncr(52, 9) * 1
print utils.ncr(52, 5)
numSim = 200000
for i in xrange(numSim):
    sim.play()
    bookeeper.recordCard(sim.dealer)
    bookeeper.recordPlayer(sim.dealer)

#check
cntCard = bookeeper.cntCard
cntPlayerWin = bookeeper.cntPlayerWins

if len(cntCard) != NUM_CARD:
    err = "FAIL: cntCard = "
    err += str(len(cntCard)) 
    sys.exit(err)
else:
    for k,v in cntCard.iteritems():
        log = k.psdisplay()
        log += ": %d" % v
        print log
        print "PASS"

if abs(cntPlayerWin[0] - cntPlayerWin[1]) / numSim > 0.01: 
    err = "FAIL: player wins: "
    err += str(cntPlayerWin[0]) 
    err += " "
    err += str(cntPlayerWin[1]) 
    sys.exit(err) 
else:
    print "player wins: "
    print cntPlayerWin.values()
    print "PASS"

