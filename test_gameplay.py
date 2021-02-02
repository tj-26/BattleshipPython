import gameplay

class TestGameplay:

    def test_board_grid(self):

        board = gameplay.Board(8)
        assert 8 == len(board.print_board())

