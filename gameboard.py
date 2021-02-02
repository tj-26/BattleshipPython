class Board:

    # mapping letters to integer value for grid index
    letters_map = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
    }

    # initialise the game board with creation of grid of size 8*8
    def __init__(self, size):
        self.size = size + 1
        self.board = [[0] * size for i in range(size)]

    # MAPPING THE USERS INPUT VALUES TO GRID INDEX VALUES TO BE USED BY LOGIC
    def map_user_input(self, row, column):
        col_index = self.letters_map.get(column)
        row_index = row - 1

        return row_index, col_index

    # method to display the board
    def print_board(self):
        index = 1
        # This prints the grid structure
        print("  " + " ".join(str(x) for x in self.letters_map.keys()))
        # this prints the actual grid
        for r in self.board:
            print(str(index)+ " " + " ".join(str(c) for c in r))
            index += 1

        return self.board

    # this method uses validation method as well as some internal validation for ship placing round for each player
    def ship_place(self, direction, row, column):
        # uses the input validation function for checking
        if self.input_validation(row, column):
            row_index, col_index = self.map_user_input(row, column)

            # checks if the ship is aligned vertically or horizontally , otherwise throws error to user
            if direction == 'v':
                if self.input_validation(row_index + 2, column):
                    for i in range(3):
                        self.board[row_index + i][col_index] = 1
                    return True
                else:
                    print("Vertical Value for ship is greater than board grid! Please Change!")
                    return False
            # checks if the ships is being placed horizontally or not
            elif direction == 'h':
                if self.input_validation(row, chr(ord(column) + 2)):
                    for i in range(3):
                        self.board[row_index][col_index + i] = 1
                    return True
                else:
                    print("Horizontal Value for ship is greater than board grid! Please Change!")
                    return False
            else:
                print("Value must be h or v!")
                return False
        else:
            print('Invalid Values Entered.!')
            return False

    # this functions defines the attack logic for each player
    def shot_fired(self, row, column):
        if self.input_validation(row, column):
            row_index, col_index = self.map_user_input(row, column)
            # checks if its a hit turns the ship coordinate to 0 and returns true
            if self.board[row_index][col_index] == 1:
                self.board[row_index][col_index] = 0
                return True
            else:
                return False
        else:
            print("Value is greater than board grid! Please Change!")
            return False

    # this function is used for validating user input
    def input_validation(self, row, column):
        row_index, col_index = self.map_user_input(row, column)
        return col_index in self.letters_map.values() and row_index in range(len(self.board)-1)


