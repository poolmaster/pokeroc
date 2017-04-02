#!/usr/bin/env python2.7

from __future__ import division

from param import *
from dealer import Dealer


simAllHands = 0
numPlayer = 2
cntTotal = 0 #total hands
cntRes = [] #win/tie/loose count for hands
odds = []


#initialize
dealer = Dealer(numPlayer, 0)
for i in xrange(NUM_HAND):
    cntRes.append([0,0])
    odds.append(0)

#simulate
for i in xrange(cntTotal):
    dealer.play()
    dealer.judge()
    for player in dealer.players:
        if not player.isPuppet and not simAllHands:
            continue
        res = dealer.getResult(player) 
        if res != LOST:
            handIdx = getHandIdx(player.cards) 
            cntRes[handIdx][res] += 1

for i in xrange(NUM_HAND):
    if cntRes[i] == [0, 0]:
        continue
    odds[i][TIE] = cntRes[TIE]/cntTotal
    odds[i][WIN] = cntRes[WIN]/cntTotal

#for i in xrange(len(dealer.players)):
#    dealer.displayPlayer(i)
#
#dealer.displayCommunity()
#
#dealer.displayWinner()

