import pygame
import constantes as cst
from labyrinth import Labyrinth


pygame.init()
"""
import module pygame for manage destination MacGyver.
"""
pygame.display.set_caption("Projet 3 : Aidez Macgyver à s'échapper !")
window = cst.pygame.display.set_mode((cst.WINDOW_HEIGHT, cst.WINDOW_WIDTH))

laby = Labyrinth("map.txt")

while laby.mac_gyver.game:
    """
    I choose module pygame for my game
    I can to change my destination (Top, Left, Up or Right) 
    """
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

# print("========= G A M E ========= O V E R ===============")
