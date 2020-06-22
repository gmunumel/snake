from game.globals import *
import pygame

class Board():
  def __init__(self, screen):

    self.board = pygame.Surface(BOARD)

    for axis in range(0, BOARD_ROWS + 1):
      pygame.draw.line(self.board, WHITE, (LEFT, TOP + (axis * SQUARE_SIZE)), (RIGHT, TOP + (axis * SQUARE_SIZE)), 1)
      pygame.draw.line(self.board, WHITE, (LEFT + (axis * SQUARE_SIZE), TOP), (LEFT + (axis * SQUARE_SIZE), BOTTOM), 1)    

    self.screen = screen


  def draw(self):
    self.screen.blit(self.board, self.board.get_rect())

  def update(self):
    a = 2
    #self.score += 1

  #def display_board(self, screen):
  #  for x in range(LEFT, RIGHT, SQUARE_SIZE):
  #    for y in range(TOP, DOWN, SQUARE_SIZE):
  #      pygame.draw.line(screen, WHITE, (x, y), (x + SQUARE_SIZE, y + SQUARE_SIZE), 1)
    