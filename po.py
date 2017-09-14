#!/usr/bin/env python2.7
from __future__ import division #force / to get float val

import sys
import argparse
import textwrap
import random
from datetime import datetime
from param import *
from sim import Sim
from deck import Card
from bookeeper import Bookeeper
import utils


#argument parser
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent("""\
    PokerOc: odds calculator for poker hands
    ----------------------------------------
    card string format:
        [Color: s,h,c,d][Rank: 2-9,T,J,Q,K,A]
        e.g. hA
    hand string format: 
        1. concatenate 2 card strings
        e.g. sAhK
        2. [Rank][Rank][isSuited?: s, o] but only valid for preflop single hand
        e.g. AKs, AKo
    """)
)
parser.add_argument('hand', action='store', nargs='+',
                     metavar='str',
                     help='list of player pocket hands')
parser.add_argument('-d', '--debug', action='store_true', default=False,
                     help='print debug logs')
parser.add_argument('-np', '--numPlayer', action='store', default=2,  
                     metavar='int',
                     help='number of players')
parser.add_argument('-c', '--com', action='store', nargs='*', default=[],
                     metavar='str',
                     help='list of cards in community pool')
parser.add_argument('-db', '--dbName', action='store', default='__stats.db',
                     metavar='str',
                     help='specify database file name')
parser.add_argument('-ns', '--numSim', action='store', type=int,
                     metavar='int',
                     help='number of simulations, better let program to decide')
args = parser.parse_args()

if args.debug:
    print "puppet hands: " + " ".join(args.hand)
    print "number of players: " + str(args.numPlayer)
    print "community cards: " + " ".join(args.com)
    print "db name: " + args.dbName
    print "number of simulation: " + str(args.numSim) 
    #sys.exit("stop")

#initialize
sim = Sim(
    numPlayer=args.numPlayer,
    numPuppet=len(args.hand),
    puppetHands=[utils.getCardList(hand) for hand in args.hand],
    propCommunity=[Card.fromStr(x.strip()) for x in args.com]
)
bookeeper = Bookeeper(args.dbName, args.debug)
numSim = utils.ncr(
    NUM_CARD, 
    (args.numPlayer - len(args.hand)) * NUM_CARD_POCKET + NUM_CARD_COMMUNITY - len(args.com)
) * 100
numSim = min(numSim, MAX_SIM)
if args.numSim != None:
    numSim = args.numSim

#simulate
random.seed(datetime.now())
for i in xrange(numSim):
    sim.play()
    bookeeper.recordGame(sim.dealer)
    if args.debug:
        sim.display()
        
#process results
if len(args.hand) == 1 and len(args.com)==0:
    #only store the 169 hands (long latency) in DB
    bookeeper.appendDB(sim.dealer, numSim)
    bookeeper.readDB()
    bookeeper.overwriteDB() 
    print "hand, winOdds, tieOdds, numSim"
    stat = bookeeper.getHandOdds(args.hand[0]) 
    print args.hand[0] + ", " + stat
else:
    if len(args.com) != 0:
        print "community cards: " + " ".join(args.com)
    print "hand, winOdds, tieOdds, numSim"
    for player in sim.dealer.puppets:
        stat = bookeeper.getPlayerOdds(player.id, numSim)
        print args.hand[player.id] + ", " + stat
        

