from param import *

class Card:
  #instance variable:
  #color
  #rank
  #id
  def __init__(self, color, rank, id):
    self.color = color 
    self.rank = rank 
    self.id = id  #unique id
  
  def compare(self, card):
    if self.rank > card.rank:
      return 1
    elif self.rank == card.rank:
      return 0
    else:
      return -1

  def display(self, prefix=""): 
    res = "" 
    res += COLOR_LIST[self.color]
    res += " "
    res += RANK_LIST[self.rank]
    print prefix+res
    return res
