import pygame as pg

pg.init()

# WINDOW PARAMETERS
NUMBER_RAW = 15
NUMBER_COLUMN = 15
SQUARE_SIZE = 32
WINDOW_HEIGHT = NUMBER_RAW * SQUARE_SIZE
WINDOW_WIDTH = NUMBER_COLUMN * SQUARE_SIZE

# LOAD PICTURES
WALL = pg.image.load("images/wall.png")
GUARDIAN = pg.image.load("images/gardian.png")
MACGYVER = pg.image.load("images/macgyver.png")
EXIT = pg.image.load("images/exit.png")
FLOOR = pg.image.load("images/floor.png")

OBJECT1 = pg.image.load("images/object1.png")
OBJECT2 = pg.image.load("images/object2.png")
OBJECT3 = pg.image.load("images/object3.png")
