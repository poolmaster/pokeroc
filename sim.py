#!/usr/bin/env python2.7

from dealer import Dealer


dealer = Dealer(2, 0)

dealer.startNewHand()
dealer.dealHandCards()
dealer.dealCommunityCards(3)
dealer.dealCommunityCards(1)
dealer.dealCommunityCards(1)

for i in xrange(len(dealer.players)):
    dealer.displayPlayer(i)

dealer.displayCommunity()

dealer.judge()
dealer.displayWinner()

