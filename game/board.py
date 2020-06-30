from game.globals import *
import pygame

class Board():
  def __init__(self, screen):
    self.board = pygame.Surface(BOARD)

    for r in range(0, BOARD_ROWS + 1):
      pygame.draw.line(self.board, WHITE, 
                      (LEFT, TOP + (r * SQUARE_SIZE)), 
                      (RIGHT, TOP + (r * SQUARE_SIZE)), 1)
      
    for c in range(0, BOARD_ROWS + 1):
      pygame.draw.line(self.board, WHITE, 
                      (LEFT + (c * SQUARE_SIZE), TOP), 
                      (LEFT + (c * SQUARE_SIZE), BOTTOM), 1)    

    self.screen = screen
    self.boardCopy = []

  def clean_board(self):
    self.boardCopy = self.board.copy()

  def display_snake(self, snake):
    for coord in snake:
      initial_x = coord[0] * SQUARE_SIZE
      initial_y = coord[1] * SQUARE_SIZE

      pygame.draw.rect(self.boardCopy, SNAKE_COLOR, 
        (LEFT + initial_x, TOP + initial_y, SQUARE_SIZE, SQUARE_SIZE))


  def display_tile(self, tile):
    initial_x = tile[0] * SQUARE_SIZE
    initial_y = tile[1] * SQUARE_SIZE
    
    pygame.draw.rect(self.boardCopy, TILE_COLOR, 
        (LEFT + initial_x, TOP + initial_y, SQUARE_SIZE, SQUARE_SIZE))

  def draw(self):
    self.screen.blit(self.boardCopy, self.boardCopy.get_rect())

    