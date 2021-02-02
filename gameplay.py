class Board:

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

    def __init__(self, size):
        self.size = size + 1
        self.board = [[0] * size for i in range(size)]

    def print_board(self):

        index = 1
        print("  " + " ".join(str(x) for x in self.letters_map.keys()))
        for r in self.board:
            print(str(index)+ " " + " ".join(str(c) for c in r))
            index += 1

        return self.board

    # def ship_place(self, direction, startpoint):


    # def input_validation(self):






A = Board(8)
A.print_board()
