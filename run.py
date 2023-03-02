from random import randint

scores = {"computer": 0, "player": 0}


class Battlefield:
    """
    Sets the size for the battle field and the size of the fleet,
    the name for the players, the type of player.
    It has methods for adding ships, for guesses and for printing the battle-field
    """
    def __init__(self, grid_size, fleet_size, name, type):
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
        # print(self.ships)
        # print(self.guesses)
        # board_size = size_conversion(self.grid_size)
        # battlefield = [["°" for row in range(board_size)] for column in range(board_size)]
        # print(battlefield)

    def random_coord(self):
        return randint(0, self.grid_size - 1)

    def add_ship(self, x, y, type):
        self.ships.append((x, y))
        if self.type == "player":
            self.battlefield[x][y] = "@"
        # elif self.type == "computer":
        #     self.battlefield[x][y] = "#"

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.battlefield[x][y] = "X"
        if (x, y) in self.ships:
            self.battlefield[x][y] = "*"
            return "Hit"
        return "Miss"


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
        if values.lower() not in ("s", "m", "l"):  # hint taken from this post https://stackoverflow.com/questions/22304500/multiple-or-condition-in-python
            raise ValueError(
                f"Enter only s (for small size), m (for medium size), or l (for large size)")
    except ValueError as e:
        print(f'Invalid data: {e}, please try again\n')
        return False
    return True

def validate_coord(x, y, player):
    """
    Check if the coordinates are numeric and if are in the correct range,
    and if it is enterd twice
    """
    try:
        t = (int(x), int(y))
        if not (all([isinstance(item, int) for item in t])): # hint taken from this post https://datascienceparichay.com/article/python-check-tuple-contains-only-numbers/
            raise ValueError(
                f'enter only integer from 0 to {player.grid_size-1}')
        elif (int(x), int(y)) in player.guesses:
            raise ValueError(
                f"You can't guess the same coordinates twice!")
        # elif int(x) not in range(player.grid_size-1) \
        #     or int(y) not in range(player.grid_size-1):
        #     raise ValueError(
        #         f'enter only integer from 0 to {player.grid_size-1}')
    except ValueError as e:
        if player.type == "player":
            return False
        print(f'Invalid data: {e}, please try again\n')
        return False
    return True


def check_new_coord():
    """
    Check if the coordinate was already choosen
    """


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

# def data_evaluation(type, data):
#     if type == "grid" and data :
# fleet = int(input('enter the size of your fleet (max.value = 7): \n'))


def x_y_gen(battlefield):
    """
    This function calls the Class function random_coord
    that generates random coordinates for x and y.
    """
    x = battlefield.random_coord()
    y = battlefield.random_coord()
    return x, y


def ship_placement(battlefield):
    """
    This function unpack the coordinates coming from
    x_y_gen function
    At the end calls the add_ship class function that adds
    the coordinates to the ships list of the class
    """
    x, y = x_y_gen(battlefield)
    battlefield.add_ship(x, y, battlefield)

    # ships = []
    # for ship in range(fleet):
    #     ships.append((random_coord(grid),random_coord(grid)))

    # print(ships)


def make_guess(player):
    """
    This function check if the player is the computer or the user.
    If it's the computer call the random coordinates generator.
    If it's the user asks to input the coordinates.
    """
    while True:
        if player.name != "Computer":
            # player = player_battlefield
            x, y = x_y_gen(player)
            if validate_coord(x, y, player):
                break
        else:
            # player = "computer_battlefield"
            
            x = input('Guess a row: \n')
            y = input('Guess a column: \n')
            if validate_coord(x, y, player):
                break
    return player.guess(int(x), int(y))


def calculate_score(result, player):
    """
    This function gets two inputs: result (Hit or Miss), and the type of player (player or Computer)
    and adds 1 to scores dictionary if it is a Hit
    """
    if result == "Hit":
        scores[player.type] += 1
    

def end_game(computer_battlefield, player_battlefield):
    '''
    This function return True if one of the players hits all the ships
    '''
    if (scores["computer"] == computer_battlefield.fleet_size) or (scores["player"] == player_battlefield.fleet_size):
        return True


def winner(computer_battlefield, player_battlefield):
    '''
    This function returns the name for the winner
    '''
    winner = max(scores)
    if winner == "player":
        winner = player_battlefield.name
    else:
        winner = computer_battlefield.name
    return winner
    

def play_game(computer_battlefield, player_battlefield):
    while True:
        print(f"{player_battlefield.name}'s battlefield")
        player_battlefield.print()
        print(f"{computer_battlefield.name}'s battlefield")
        computer_battlefield.print()
        computer_guess = make_guess(player_battlefield)
        player_guess = make_guess(computer_battlefield)
        print(f'{player_battlefield.name} got a {player_guess}, guessing {computer_battlefield.guesses[-1]}')
        print(f'{computer_battlefield.name} got a {computer_guess}, guessing {player_battlefield.guesses[-1]}')
        calculate_score(player_guess, player_battlefield)
        calculate_score(computer_guess, computer_battlefield)
        print('-'*40)
        print('-'*40)
        print('-'*16 + " SCORE " + "-"*16)
        print(f"{player_battlefield.name}: {(scores['player'])}  ||  {computer_battlefield.name}: {(scores['computer'])}")
        if end_game(computer_battlefield, player_battlefield):
            break
    print('-'*16 + " GAME OVER " + "-"*16)
    winner_name = winner(computer_battlefield, player_battlefield)
    print(f'The winner is {winner_name}')

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

    for ship in range(fleet_size):
        ship_placement(player_battlefield)
        ship_placement(computer_battlefield)
    
    play_game(computer_battlefield, player_battlefield)


new_match()
