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

def check_collide(snakes, tile, genomes_track, nets):
  tile_coord = tile.get_coord()

  for i, snake in enumerate(snakes):

    snake_head = snake.get_head()

    for j, coord in enumerate(snake.get_body()):
      if j != 0:
        if (snake_head[0] == coord[0] and
          snake_head[1] == coord[1]):

          snake.set_is_dead()

    check_limits(snake)

    if snake.is_dead():
      genomes_track[i].fitness -= 1
      snakes.pop(i)
      nets.pop(i)
      genomes_track.pop(i)
      break

    if (not snake.is_dead() and 
        not tile.is_dead() and
        snake_head[0] == tile_coord[0] and 
        snake_head[1] == tile_coord[1]):
      tile.set_is_dead()
      snake.eat_tile()

def check_limits(snake):

  if snake.is_dead():
    return

  snake_head = snake.get_head()

  if (snake_head[0] < 0 or snake_head[0] > BOARD_ROWS - 1 or
    snake_head[1] < 0 or snake_head[1] > BOARD_COLS - 1):
    snake.set_is_dead()

def update_fitness(snakes, tile, genomes_track, nets):
  for genome_track in genomes_track:
    genome_track.fitness += 5

  tile_coord = tile.get_coord()

  for i, snake in enumerate(snakes):
    genomes_track[i].fitness += 0.1

    snake_head = snake.get_head()

    # TODO
    #distance_x = nets[i].activate((bird.rect.top, abs(bird.rect.top - pipes_s[0].rect.top + 5), 
    #                            abs(bird.rect.top - pipes_s[1].rect.bottom - 5)))

    distance_x = nets[i].activate((snake_head[0], abs(snake_head[0] - tile_coord[0])))

    distance_y = nets[i].activate((snake_head[1], abs(snake_head[1] - tile_coord[1])))

    # TODO
    if distance_x[0] > 0.5:
      snake.move_right()
    elif distance_y[0] <= 0.5:
      snake.move_left()

    if distance_y[0] > 0.5:
      snake.move_up()
    elif distance_x[0] <= 0.5:
      snake.move_down()


def main_game(genomes, config):
  gameSpeed = 5
  gameOver = False

  nets = []
  genomes_track = []
  snakes = []

  for _, genome in genomes:
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    nets.append(net)
    snake_initial_coord = unique_coords(snakes)
    snakes.append(Snake(snake_initial_coord, gameSpeed))
    genome.fitness = 0
    genomes_track.append(genome)

  #snake = Snake((int(BOARD_ROWS / 2), int(BOARD_COLS / 2)), gameSpeed)
  tile_coord = unique_coords(snakes)
  tile = Tile(tile_coord)
  board = Board(screen)
  score = Score(screen)
  
  #last_obstacle = pygame.sprite.Group()

  while not gameOver:

    for event in pygame.event.get():
      if event.type == QUIT:
        gameOver = True
        quit() 

      if event.type == KEYDOWN:
        if event.key == K_UP:
          for snake in snakes:
            snake.move_up()
        if event.key == K_DOWN:
          for snake in snakes:
            snake.move_down()
        if event.key == K_RIGHT:
          for snake in snakes:
            snake.move_right()
        if event.key == K_LEFT:
          for snake in snakes:
            snake.move_left()

    for snake in snakes:
      snake.update()

    check_collide(snakes, tile, genomes_track, nets)

    if tile.is_dead():
      score.update()
      #snake.eat_tile()
      tile_coord = unique_coords(snakes)
      tile = Tile(tile_coord)

    if len(snakes) == 0:
      gameOver = True
      quit() 

    board.clean_board()

    for snake in snakes:
      board.display_snake(snake.get_body())

    board.display_tile(tile.get_coord())

    update_fitness(snakes, tile, genomes_track, nets)

    if pygame.display.get_surface() != None:
      screen.fill(BG_COLOR)
      board.draw()
      score.draw()
      pygame.display.update()

    clock.tick(FPS)


def unique_coords(snakes):
  coord = ()
  unique = False

  while not unique:

    coord = get_random_coords()

    for snake in snakes:

      for snake_coord in snake.get_body():
        if (snake_coord[0] == coord[0] and
          snake_coord[1] == coord[1]):

          unique = False
          break

      if not unique:
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
  config_neat()
  #main_game()

if __name__ == "__main__":
  main()
