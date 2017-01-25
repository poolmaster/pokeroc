#52-card deck

import random
from param import *
from card import Card

class Deck: 
  #instance variable
  #cards[]
  #nextCard  #pointer
  def __init__(self):
    self.cards = []
    id = 0
    for i in range(NUM_COLOR):
      for j in range(NUM_RANK):
        newCard = Card(i, j, id)
        self.cards.append(newCard)
        id = id + 1
    self.nextCard = 0
  
  def shuffle(self):
    for i in range(0, NUM_CARD - 1):
      randIndex = random.randrange(i, NUM_CARD) 
      self.cards[i], self.cards[randIndex] = self.cards[randIndex], self.cards[i] 
    self.nextCard = 0
 
  #just switch the card (target) with card of the target position in the deck
  def setCard(position, card):
    for i in range(len(self.cards)):
      if self.cards[i].color == card.color and self.cards[i].rank == card.rank:
        self.cards[i], self.cards[position] = self.cards[position], self.cards[i]      

  def getNext(self):
    card = self.cards[self.nextCard]
    self.nextCard += 1 
    return card
      
  
