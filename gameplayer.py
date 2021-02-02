from gameboard import Board

class Player:

    # setting a counter for keeping track of sink condition
    counter = 0

    # initializing name of player and board object
    def __init__(self, name):
        self.name = name
        self.board = Board(8)

    # method to place ships for each player object
    def player_ship_placing(self, direction, row, column):
        ship_status = self.board.ship_place(direction, int(row), column)
        self.board.print_board()
        return ship_status

    # method for attack rounds for each player
    def player_shots_fired(self, player_board_object, row, column):

        #  initially checks if player has hit the ship
        if player_board_object.shot_fired(int(row), column):

            #  increments the counter
            self.counter += 1

            # checks if sink condition is true
            if self.is_sink():
                print("Ship is Sinked..!")
                return True
            else:
                print("Ship is Hit..!")
            return True
        else:
            print("Ship is Missed..!")
            return False

    # method to check if counter value is 3 for sink condition
    def is_sink(self):
        return self.counter == 3

    # validating the correct input by user
    def input_validation(self, ship_d, ship_r, ship_c):
        return ship_d == 'h' or 'v' and ship_r.isnumeric() and type(ship_c) == str








