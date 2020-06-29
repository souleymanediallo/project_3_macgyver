import pygame

pygame.display.init()
pygame.display.set_mode()

# WINDOW PARAMETERS
NUMBER_RAW = 15
NUMBER_COLUMN = 15
SQUARE_SIZE = 32
WINDOW_HEIGHT = NUMBER_RAW * SQUARE_SIZE
WINDOW_WIDTH = NUMBER_COLUMN * SQUARE_SIZE

# LOAD PICTURES
WALL = pygame.image.load("images/wall.png")
GUARDIAN = pygame.image.load("images/gardian.png")
MACGYVER = pygame.image.load("images/macgyver.png")
EXIT = pygame.image.load("images/exit.png")
FLOOR = pygame.image.load("images/floor.png")


OBJECT1 = pygame.image.load("images/object1.png")
OBJECT2 = pygame.image.load("images/object2.png")
OBJECT3 = pygame.image.load("images/object3.png")


