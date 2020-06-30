class MacGyver:
    """
    structure of my class MacGyver
    create and fill this list when MG encounters an object (check collision method)
    """
    def __init__(self, map):
        self.game = True
        self.map = map
        self.search_m()
        self.list_objects = []

    def search_m(self):
        """ search position MacGyver : position_x et position_y raw and column """
        for y, letter in enumerate(self.map):
            for x, line in enumerate(letter):
                if line == "M":
                    self.position_x = x
                    self.position_y = y

    def move_m(self, item):
        """
        position an object in the file
        put an item at mac_gyver position
        """
        self.map[self.position_y][self.position_x] = item

    def move_to(self, go_to):
        """ Positionner MacGyver and destination (Top, Left, Bottom or Right) """
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

    def check_collision(self, x, y):
        """ manage the movements of MG with respect to objects and the guardian """
        n_columns = len(self.map[0])
        n_raws = len(self.map)

        if self.map[x][y] == "x":
            return False  # move not OK
        elif x < 0 or y < 0 or x > (n_columns - 1) or y > (n_raws - 1):
            return False  # move not OK

        elif self.map[x][y] == "T" or self.map[x][y] == "E" or self.map[x][y] == "A":
            self.list_objects.append(self.map[x][y])
            # print(self.list_objects)
            return True  # move Ok

        # Gardian
        elif self.map[x][y] == 'G':
            if len(self.list_objects) == 3:
                return True
            else:
                self.game = False
                print("Game Over")
                return False

        elif self.map[x][y] == "S":
            print("================ You have to win the game, Congratulations !!! ===============")
            self.game = False
            return True  # move OK

        else:
            return True
