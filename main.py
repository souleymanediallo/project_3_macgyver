from constantes import *
from labyrinth import Labyrinth
import pygame

pygame.init()
pygame.display.set_caption("Projet 3 : Aidez Macgyver à s'échapper !")
window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

laby = Labyrinth("map.txt")

while laby.mac_gyver.game:
    # it's my labyrinth
    laby.show_labyrinth(window)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            laby.mac_gyver.game = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                laby.mac_gyver.move_to("L")
            elif event.key == pygame.K_RIGHT:
                laby.mac_gyver.move_to("R")
            elif event.key == pygame.K_UP:
                laby.mac_gyver.move_to("U")
            elif event.key == pygame.K_DOWN:
                laby.mac_gyver.move_to("D")


# print("========================= G A M E ========= O V E R ===============================")

