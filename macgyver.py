class MacGyver:
    # structure of my class MacGyver
    def __init__(self, map):
        self.game = True
        self.map = map
        self.search_m()
        self.list_objects = []  # créer et remplir cette liste quand MG rencontre un objet (methode check collision)

    def search_m(self):
        for y, letter in enumerate(self.map):
            for x, line in enumerate(letter):
                if line == "M":
                    self.position_x = x
                    self.position_y = y

    # position an object in the file
    # put an item at mac_gyver position
    def move_m(self, item):
        self.map[self.position_y][self.position_x] = item

    # Positionner MacGyver
    def move_to(self, go_to):
        self.move_m(' ')  # replace macgyver with an empty box
        if go_to == "L":
            if self.check_collision(self.position_y, self.position_x - 1):
                self.position_x -= 1
        elif go_to == "R":
            if self.check_collision(self.position_y, self.position_x + 1):
                self.position_x += 1
        elif go_to == "U":
            if self.check_collision(self.position_y - 1, self.position_x):
                self.position_y -= 1
        elif go_to == "D":
            if self.check_collision(self.position_y + 1, self.position_x):
                self.position_y += 1
        else:
            print("Go to : L, R, U, D")

        self.move_m("M")

    # manage the movements of MG with respect to objects and the guard
    def check_collision(self, x, y):
        n_columns = len(self.map[0])
        n_raws = len(self.map)

        if self.map[x][y] == "x":
            return False   # move not OK
        elif x < 0 or y < 0 or x > (n_columns - 1) or y > (n_raws - 1):
            return False   # move not OK

        elif self.map[x][y] == "T" or self.map[x][y] == "E" or self.map[x][y] == "A":
            self.list_objects.append(self.map[x][y])
            # print(self.list_objects)
            return True    # move Ok

        # Gardian
        elif self.map[x][y] == 'G':
            if len(self.list_objects) == 3:
                return True
            else:
                return False

        elif self.map[x][y] == "S":
            print("================ You have to win the game, Congratulations !!! ===============")
            self.game = False
            return True  # move OK

        else:
            return True


