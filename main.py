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

def check_collide(snake, tile):
  tile_coord = tile.get_coord()
  snake_head = snake.get_head()

  for i, coord in enumerate(snake.get_body()):
    if i != 0:
      if (snake_head[0] == coord[0] and
        snake_head[1] == coord[1]):

        snake.set_is_dead()
        break

  if (not snake.is_dead() and 
      snake_head[0] == tile_coord[0] and 
      snake_head[1] == tile_coord[1]):
    tile.set_is_dead()

def check_limits(snake):
  snake_head = snake.get_head()

  if (snake_head[0] < 0 or snake_head[0] > BOARD_ROWS - 1 or
    snake_head[1] < 0 or snake_head[1] > BOARD_COLS - 1):
    snake.set_is_dead()

def main_game():
  gameSpeed = 10
  gameOver = False

  snake = Snake((int(BOARD_ROWS / 2), int(BOARD_COLS / 2)), gameSpeed)
  tile_coord = unique_coords(snake.get_body())
  tile = Tile(tile_coord)
  board = Board(screen)
  score = Score(screen)
  
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

    check_limits(snake)
    check_collide(snake, tile)

    if snake.is_dead():
      gameOver = True
      quit()

    if tile.is_dead():
      score.update()
      snake.eat_tile()
      tile_coord = unique_coords(snake.get_body())
      tile = Tile(tile_coord)

    board.update(snake.get_body(), tile.get_coord())

    if pygame.display.get_surface() != None:
      screen.fill(BG_COLOR)
      board.draw()
      score.draw()
      pygame.display.update()

    clock.tick(FPS)


def unique_coords(snake_coords):
  coord = ()
  unique = False

  while not unique:
    coord = get_random_coords()

    for snake_coord in snake_coords:
      if (snake_coord[0] == coord[0] and
        snake_coord[1] == coord[1]):

        unique = False
        break

    unique = True

  return coord

def get_random_coords():
  return (random.randrange(0, BOARD_ROWS), 
          random.randrange(0, BOARD_COLS))

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
