WIN_HEIGHT = 500
WIN_WIDTH = 500

WHITE = (255,255,255)
BG_COLOR = (0, 0, 0)

SQUARE_SIZE = 10

TOP = int(WIN_HEIGHT * 0.10)
LEFT = int(WIN_WIDTH * 0.10)
RIGHT = int(WIN_WIDTH * 0.90)
BOTTOM = int(WIN_HEIGHT * 0.90)

BOARD_ROWS = int(abs(RIGHT - LEFT) / SQUARE_SIZE)
BOARD_COLS = int(abs(BOTTOM - TOP)/ SQUARE_SIZE)

BOARD = (RIGHT + 1, BOTTOM + 1)
