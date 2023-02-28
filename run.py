from random import randint

scores = {"computer": 0, "player": 0}

class Battlefield:
    """
    Sets the size for the battle field and the size of the fleet,
    the name for the players, the type of player.
    It has methods for adding ships, for guesses and for printing the battle-field
    """
    def __init__(self,grid_size, fleet_size, name, type):
        self.grid_size = grid_size
        self.battlefield = [["°" for row in range(grid_size)] for column in range(grid_size)]
        self.fleet_size = fleet_size
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.battlefield:
            print(" ".join(row))
        # board_size = size_conversion(self.grid_size)
        # battlefield = [["°" for row in range(board_size)] for column in range(board_size)]
        # print(battlefield)

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
    real_size = size_conversion(size)
    return real_size

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

def size_conversion(value):
    """
    Convert the string value into fixed integer value
    """
    real_size = 0
    if value == "s":
        real_size = 3
    elif value == "m":
        real_size = 5
    elif value == "l":
        real_size = 7
    
    return real_size
        


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

#def populate_board

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
    
    computer_battlefield = Battlefield(grid_size, fleet_size, "Computer", type="computer")
    player_battlefield = Battlefield(grid_size, fleet_size, player, type="player")

    player_battlefield.print()

new_match()
