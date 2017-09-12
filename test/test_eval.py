#!/usr/bin/env python2.7

import sys
sys.path.append("..")

from handGen import HandGen
from evaluator import *
import utils

def checkHandVal(act, exp):
    res = "PASS"
    if act != exp:
        res = "FAIL:"
        res += " act=" + act.psdisplay()
        res += " exp=" + exp.psdisplay()
        sys.exit(res + "\n")
    print res
    return res

def checkCompare(ref, win, lose):
    w = ref.evaluate(win)
    l = ref.evaluate(lose)
    if w < l or w == l: 
        print "hand_win: " + utils.displayCards(win)
        print "eval: " + w.display()
        print "hand_lose: " + utils.displayCards(lose)
        print "eval: " + l.display()
        sys.exit("FAIL")
    else:
        print "PASS"

#evaluator under test
ref_UT = Evaluator()

#direct tests
hand_1 = utils.getCardList("sA, sK, sQ, sJ, sT, hQ, c2") 
hand_1_lose = utils.getCardList("sA, hK, hQ, hJ, hT, h9, c2") 
print "hand_1: " + utils.displayCards(hand_1)
checkHandVal(ref_UT.evaluate(hand_1), HandVal.fromStr("straight_flush", 13))
checkHandVal(ref_UT.evaluate(hand_1_lose), HandVal.fromStr("straight_flush", 12))
checkCompare(ref_UT, hand_1, hand_1_lose)

hand_2 = utils.getCardList("sT, hT, dT, cT, s3, h3, c3") 
hand_2_lose = utils.getCardList("c2, h2, d2, s2, s3, h3, c3") 
print "hand_2: " + utils.displayCards(hand_2)
checkHandVal(ref_UT.evaluate(hand_2), HandVal.fromStr("quads", 0b1000000000000000000010))
checkHandVal(ref_UT.evaluate(hand_2_lose), HandVal.fromStr("quads", 0b10000000000010))
checkCompare(ref_UT, hand_2, hand_2_lose)

hand_3 = utils.getCardList("s3, hT, dQ, cQ, d3, h3, c4") 
hand_3_lose = utils.getCardList("s3, hT, dJ, cJ, d3, h3, c4") 
hand_3_lose_lose = utils.getCardList("s2, hT, dK, cK, d2, h2, c4") 
print "hand_3: " + utils.displayCards(hand_3)
checkHandVal(ref_UT.evaluate(hand_3), HandVal.fromStr("full_house", 0b100010000000000))
checkHandVal(ref_UT.evaluate(hand_3_lose), HandVal.fromStr("full_house", 0b100001000000000))
checkHandVal(ref_UT.evaluate(hand_3_lose_lose), HandVal.fromStr("full_house", 0b10100000000000))
checkCompare(ref_UT, hand_3, hand_3_lose)
checkCompare(ref_UT, hand_3, hand_3_lose_lose)
checkCompare(ref_UT, hand_3_lose, hand_3_lose_lose)

hand_4 = utils.getCardList("sT, sK, s8, s7, s3, cQ, cK") 
hand_4_lose = utils.getCardList("hT, hK, h8, h7, h2, cQ, cK") 
hand_4_lose_lose = utils.getCardList("hJ, hQ, h8, h7, h2, cQ, cK") 
print "hand_4: " + utils.displayCards(hand_4)
checkHandVal(ref_UT.evaluate(hand_4), HandVal.fromStr("flush", 0b100101100010))
checkHandVal(ref_UT.evaluate(hand_4_lose), HandVal.fromStr("flush", 0b100101100001))
checkHandVal(ref_UT.evaluate(hand_4_lose_lose), HandVal.fromStr("flush", 0b11001100001))
checkCompare(ref_UT, hand_4, hand_4_lose)
checkCompare(ref_UT, hand_4, hand_4_lose_lose)

hand_5 = utils.getCardList("s5, hT, d7, c8, d9, h6, c4") 
hand_5_lose = utils.getCardList("s5, hj, d7, c8, d9, h6, c4") 
print "hand_5: " + utils.displayCards(hand_5)
checkHandVal(ref_UT.evaluate(hand_5), HandVal.fromStr("straight", 9))
checkHandVal(ref_UT.evaluate(hand_5_lose), HandVal.fromStr("straight", 8))
checkCompare(ref_UT, hand_5, hand_5_lose)

hand_6 = utils.getCardList("sk, hK, dK, cJ, d9, h5, c4") 
hand_6_lose = utils.getCardList("sk, hK, dK, cT, d9, h5, c4") 
print "hand_6: " + utils.displayCards(hand_6)
checkHandVal(ref_UT.evaluate(hand_6), HandVal.fromStr("set", 0b1000000000000001010000000))
checkHandVal(ref_UT.evaluate(hand_6_lose), HandVal.fromStr("set", 0b1000000000000000110000000))
checkCompare(ref_UT, hand_6, hand_6_lose)

hand_7 = utils.getCardList("s5, hT, dJ, cJ, d9, h5, c4") 
hand_7_lose = utils.getCardList("s5, hA, dJ, cJ, d9, h4, c4") 
print "hand_7: " + utils.displayCards(hand_7)
checkHandVal(ref_UT.evaluate(hand_7), HandVal.fromStr("two_pair", 0b10000010000000100000000))
checkHandVal(ref_UT.evaluate(hand_7_lose), HandVal.fromStr("two_pair", 0b10000001001000000000000))
checkCompare(ref_UT, hand_7, hand_7_lose)

hand_8 = utils.getCardList("s5, hK, d8, cJ, d9, h5, c4") 
hand_8_lose = utils.getCardList("s4, hA, d8, cJ, d9, h5, c4") 
print "hand_8: " + utils.displayCards(hand_8)
checkHandVal(ref_UT.evaluate(hand_8), HandVal.fromStr("one_pair", 0b00000010000101010000000))
checkHandVal(ref_UT.evaluate(hand_8_lose), HandVal.fromStr("one_pair", 0b00000001001001010000000))
checkCompare(ref_UT, hand_8, hand_8_lose)

hand_9 = utils.getCardList("sA, hK, dQ, cJ, d9, h5, c4") 
print "hand_9: " + utils.displayCards(hand_9)
checkHandVal(ref_UT.evaluate(hand_9), HandVal.fromStr("high_card", 0b1111010000000))

checkCompare(ref_UT, hand_1, hand_2)
checkCompare(ref_UT, hand_1, hand_3)
checkCompare(ref_UT, hand_1, hand_4)
checkCompare(ref_UT, hand_1, hand_5)
checkCompare(ref_UT, hand_1, hand_6)
checkCompare(ref_UT, hand_1, hand_7)
checkCompare(ref_UT, hand_1, hand_8)
checkCompare(ref_UT, hand_1, hand_9)

checkCompare(ref_UT, hand_2, hand_3)
checkCompare(ref_UT, hand_2, hand_4)
checkCompare(ref_UT, hand_2, hand_5)
checkCompare(ref_UT, hand_2, hand_6)
checkCompare(ref_UT, hand_2, hand_7)
checkCompare(ref_UT, hand_2, hand_8)
checkCompare(ref_UT, hand_2, hand_9)

checkCompare(ref_UT, hand_3, hand_4)
checkCompare(ref_UT, hand_3, hand_5)
checkCompare(ref_UT, hand_3, hand_6)
checkCompare(ref_UT, hand_3, hand_7)
checkCompare(ref_UT, hand_3, hand_8)
checkCompare(ref_UT, hand_3, hand_9)

checkCompare(ref_UT, hand_4, hand_5)
checkCompare(ref_UT, hand_4, hand_6)
checkCompare(ref_UT, hand_4, hand_7)
checkCompare(ref_UT, hand_4, hand_8)
checkCompare(ref_UT, hand_4, hand_9)

checkCompare(ref_UT, hand_5, hand_6)
checkCompare(ref_UT, hand_5, hand_7)
checkCompare(ref_UT, hand_5, hand_8)
checkCompare(ref_UT, hand_5, hand_9)

checkCompare(ref_UT, hand_6, hand_7)
checkCompare(ref_UT, hand_6, hand_8)
checkCompare(ref_UT, hand_6, hand_9)

checkCompare(ref_UT, hand_7, hand_8)
checkCompare(ref_UT, hand_7, hand_9)

checkCompare(ref_UT, hand_8, hand_9)

#random tests
handGen = HandGen(5)

