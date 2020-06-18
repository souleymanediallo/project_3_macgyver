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

    def show_labyrinth(self):
        for line in self.map:
            chaine_caract = ""
            for l in line:
                chaine_caract += l
            print(chaine_caract)

    def position_object(self):
        n_columns = len(self.map[0])
        n_raws = len(self.map)

        for value in self.dico_laby.values():
            random_x = random.randint(0, n_columns - 1)
            random_y = random.randint(0, n_raws - 1)
            while self.map[random_x][random_y] != " ":
                random_x = random.randint(0, n_columns - 1)
                random_y = random.randint(0, n_raws - 1)
            self.map[random_x][random_y] = value
