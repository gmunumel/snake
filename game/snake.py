from game.globals import *
from enum import Enum

class Snake():
  def __init__(self, head, gameSpeed):
    self.gameSpeed = gameSpeed
    self.count = 0
    self.direction = Direction.RIGHT
    self.body = []
    self.body.append(head)
    self.head = self.body[0]
    self.tail = self.body[-1]
    self.isDead = False
    self.oldTail = ()
  
  def get_head(self):
    return self.body[0]

  def get_tail(self):
    return self.body[-1]

  def get_body(self):
    return self.body

  def get_direction(self):
    return self.direction

  def move_right(self):
    if self.direction != Direction.RIGHT:
      self.direction = Direction.RIGHT

  def move_up(self):
    if self.direction != Direction.UP:
      self.direction = Direction.UP

  def move_left(self):
    if self.direction != Direction.LEFT:
      self.direction = Direction.LEFT

  def move_down(self):
    if self.direction != Direction.DOWN:
      self.direction = Direction.DOWN

  def is_dead(self):
    return self.isDead

  def set_is_dead(self):
    self.isDead = True

  def set_game_speed(self, gameSpeed):
    self.gameSpeed = gameSpeed

  def eat_tile(self):
    self.body.append(self.oldTail)

  def update(self):
    if self.count > self.gameSpeed:
      x = self.get_head()[0]
      y = self.get_head()[1]

      self.oldTail = self.get_tail()

      if self.direction == Direction.RIGHT:
        x += 1
      if self.direction == Direction.UP:
        y -= 1
      if self.direction == Direction.LEFT:
        x -= 1
      if self.direction == Direction.DOWN:
        y += 1

      self.body.insert(0, (x, y))
      self.body.pop(len(self.body) - 1)

      self.count = 0

    self.count += 1

  def print_body(self):
    for i in range(len(self.body)):
      print('({}, {})'.format(self.body[i][0], self.body[i][1]))


class Direction(Enum):
  RIGHT = 1
  UP = 2
  LEFT = 3
  DOWN = 4