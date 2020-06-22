from game.globals import *

class Snake():
  def __init__(self, screen):
    self.image = ''
    self.screen = screen

  def draw(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    self.screen.blit(self.image, self.rect)