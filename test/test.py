#tests
from handGen import HandGen
from evaluator import Evaluator


handGen = HandGen(5)
winHand = handGen.getRandomHand()
loseHand = handGen.getRandomHand()

ref_UT = Evaluator(winHand)
winRank, winVal = ref_UT.handRank, ref_UT.value
ref_UT.updateCards(loseHand)
loseRank, loseVal = ref_UT.handRank, ref_UT.value

#todo better to have a comparator  
#todo count occurrence of each hand
#check random distribution


