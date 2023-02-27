from random import randint

scores = {"computer": 0, "player": 0}

def input_size(kind):
    """
    Get the user input for the size of the grid.
    Running a while loop to ensure the data is valid.
    It will loop until the data entered is valid.
    """
    
    while True:
        size = input(f'enter the size of your {kind} (small = s, medium = m, large = l ): \n')
        if validate_data(size):
            break
    return size

def validate_data(values):
    """
    Inside the try converts the str to small caps,
    and raises ValueError if the input is different than s,m, or l
    """
    try:
        if values.lower() not in ("s","m","l") : #hint taken from this post https://stackoverflow.com/questions/22304500/multiple-or-condition-in-python
            raise ValueError(
                f"Enter only s (for small size), m (for medium size), or l (for large size)")
    except ValueError as e:
        print(f'Invalid data: {e}, please try again\n')
        return False

    return True


def random_coord(grid):
    return randint(0, grid - 1)

# def data_evaluation(type, data):
#     if type == "grid" and data :




# fleet = int(input('enter the size of your fleet (max.value = 7): \n'))


def ship_placement():
    ships = []
    for ship in range(fleet):
        ships.append((random_coord(grid),random_coord(grid)))

    print(ships)

def new_match():
    """
    Starts a new match running all program functions
    and resetting the scores
    """
    scores["computer"] = 0
    scores["player"] = 0
    print(">"*20 + "<"*20)
    print(">> Welcome to <<Ultimate Battleship>> <<")
    print(">"*20 + "<"*20)
    player = input('enter your name: \n')
    print(">"*20 + "<"*20)
    grid_size = input_size("grid")
    fleet_size = input_size("fleet")
    print(grid_size)
    print(fleet_size)

new_match()
