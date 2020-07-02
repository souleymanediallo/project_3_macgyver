import pygame as pg

import constantes as cst
from labyrinth import Labyrinth


def main():
    """ Main function """
    pg.init()
    pg.display.set_caption("Projet 3 : Aidez Macgyver à s'échapper !")
    window = pg.display.set_mode((cst.WINDOW_HEIGHT, cst.WINDOW_WIDTH))
    laby = Labyrinth("map.txt")

    while laby.mac_gyver.game:
        """I choose module pygame for the move
        I can to change my destination (Top, Left, Up or Right)"""
        laby.show_labyrinth(window)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                laby.mac_gyver.game = False
                pg.quit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    laby.mac_gyver.move_to("L")
                elif event.key == pg.K_RIGHT:
                    laby.mac_gyver.move_to("R")
                elif event.key == pg.K_UP:
                    laby.mac_gyver.move_to("U")
                elif event.key == pg.K_DOWN:
                    laby.mac_gyver.move_to("D")


if __name__ == '__main__':
    main()
