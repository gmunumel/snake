from game.globals import *
import random

class Tile():
  def __init__(self, coord):
    self.isDead = False
    self.x = coord[0]
    self.y = coord[1]

  def set_coord(coord):
    self.x = coord[0]
    self.y = coord[1]

  def get_coord(self):
    return (self.x, self.y)

  def is_dead(self):
    return self.isDead

  def set_is_dead(self):
    self.isDead = True