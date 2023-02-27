from random import randint

scores = {"computer": 0, "player": 0}

def random_coord(grid):
    return randint(0, grid - 1)

player = input('enter your name: \n')
grid = int(input('enter the size of your battle field (max.value = 6)'))
fleet = int(input('enter the size of your fleet (max.value = 5)'))
ships = []

for ship in range(fleet):
    ships.append((random_coord(grid),random_coord(grid)))

print(ships)

