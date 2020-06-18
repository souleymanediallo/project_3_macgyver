from labyrinth import Labyrinth

laby = Labyrinth("map.txt")
laby.show_labyrinth()

while laby.mac_gyver.game:
    direction = input("What direction ? : L, R, U, D > ")
    if direction == "L":
        laby.mac_gyver.move_to("L")
    elif direction == "R":
        laby.mac_gyver.move_to("R")
    elif direction == "U":
        laby.mac_gyver.move_to("U")
    elif direction == "D":
        laby.mac_gyver.move_to("D")
    else:
        print("Déplacement impossible")

    laby.show_labyrinth()

print("========================= G A M E ========= O V E R ===============================")