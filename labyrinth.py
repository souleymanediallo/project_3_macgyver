from constantes import *
from macgyver import MacGyver
import random


class Labyrinth:
    def __init__(self, carte):
        self.carte = carte
        self.dico_laby = {"aiguille": 'A', "tube": 'T', "ether": 'E'}
        self.map = []
        self.load_labyrinth()
        self.mac_gyver = MacGyver(self.map)

    def load_labyrinth(self):
        with open(self.carte, "r") as laby:
            for line in laby.readlines():
                line_n = []
                for n in line:
                    if n != '\n':
                        line_n.append(n)
                self.map.append(line_n)
        self.position_object()

    def show_labyrinth(self, window):
        number_ligne = 0
        for line in self.map:
            number_case = 0
            for element in line:
                x = number_case * SQUARE_SIZE
                y = number_ligne * SQUARE_SIZE
                if element == "M":
                    window.blit(MACGYVER, (x, y))
                elif element == "S":
                    window.blit(EXIT, (x, y))
                elif element == "x":
                    window.blit(WALL, (x, y))
                elif element == "G":
                    window.blit(GUARDIAN, (x, y))
                elif element == "A":
                    window.blit(OBJECT1, (x, y))
                elif element == "E":
                    window.blit(OBJECT2, (x, y))
                elif element == "T":
                    window.blit(OBJECT3, (x, y))
                elif element == " ":
                    window.blit(FLOOR, (x, y))
                number_case += 1
            number_ligne += 1

    def position_object(self):
        n_columns = len(self.map[0])
        n_raws = len(self.map)

        # placer les 3 objets en vérifiant si l'emplacement est vide (pas de mur, pas d'objets)
        for value in self.dico_laby.values():
            random_x = random.randint(0, n_columns - 1)
            random_y = random.randint(0, n_raws - 1)
            while self.map[random_x][random_y] != " ":
                random_x = random.randint(0, n_columns - 1)
                random_y = random.randint(0, n_raws - 1)
            self.map[random_x][random_y] = value
