from game.globals import *
import random

class Tile():
  def __init__(self, coord):
    self.x = coord[0]
    self.y = coord[1]

  def set_coord(coord):
    self.x = coord[0]
    self.y = coord[1]

  def get_coord(self):
    return (self.x, self.y)