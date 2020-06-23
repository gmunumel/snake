from game.score import Score
from game.snake import Snake
from game.board import Board
from game.tile import Tile
from game.globals import *
from pygame.locals import *
import os, pygame, sys, random, neat

pygame.init()

srcSize = (WIN_WIDTH, WIN_HEIGHT)
FPS = 30

screen = pygame.display.set_mode(srcSize)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

def main_game():
  gameSpeed = 2
  gameOver = False

  board = Board(screen)
  score = Score(screen)
  snake = Snake((int(BOARD_ROWS / 2), int(BOARD_COLS / 2)))

  last_obstacle = pygame.sprite.Group()

  while not gameOver:

    for event in pygame.event.get():
      if event.type == QUIT:
        gameOver = True
        quit() 

      if event.type == KEYDOWN:
        if event.key == K_UP:
          snake.move_up()
        if event.key == K_DOWN:
          snake.move_down()
        if event.key == K_RIGHT:
          snake.move_right()
        if event.key == K_LEFT:
          snake.move_left()

    snake.update()
    #snake.print_body()
    board.update(snake.get_body())
    score.update()

    if pygame.display.get_surface() != None:
      screen.fill(BG_COLOR)
      board.draw()
      score.draw()

      pygame.display.update()

    clock.tick(FPS)


def run_neat(config_path):
  config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
    neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

  population = neat.Population(config)

  population.add_reporter(neat.StdOutReporter(True))
  stats = neat.StatisticsReporter()
  population.add_reporter(stats)

  winner = population.run(
    main_game, #fitness function
    50 # maximum number of iterations to run
  )

  print('\nBest genome:\n{!s}'.format(winner))

def config_neat():
  local_dir = os.path.dirname(__file__)
  config_path = os.path.join(local_dir, "neat/config-feedforward.txt")
  run_neat(config_path)

def quit():
  pygame.quit()
  sys.exit()

def main():
  #config_neat()
  main_game()

if __name__ == "__main__":
  main()
