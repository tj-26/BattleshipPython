from gameboard import Board
from gameplayer import Player
import unittest

class MyTestCase(unittest.TestCase):

    def test_board_grid(self):
        board = Board(8)
        assert 8 == len(board.print_board())

    def test_user_map(self):
        board = Board(8)
        assert 7, 0 == board.map_user_input(8, 'A')

    def test_user_map2(self):
        board = Board(8)
        assert 7, 0 != board.map_user_input(5, 'A')

    def test_ship_placed(self):
        board = Board(8)
        assert True == board.ship_place('h', 1, 'A')

    def test_ship_placed2(self):
        board = Board(8)
        assert False == board.ship_place('K', 1, 'D')

    def test_ship_placed3(self):
        board = Board(8)
        assert True == board.ship_place('h', 4, 'D')

    def test_ship_placed4(self):
        board = Board(8)
        assert False == board.ship_place('h', 1, 'X')

    def test_ship_placed5(self):
        board = Board(8)
        assert False == board.ship_place('g', 5, 'X')

    def test_ship_placed6(self):
        board = Board(8)
        assert False == board.ship_place('h', 9, 'X')

    def test_ship_placed7(self):
        board = Board(8)
        assert False == board.ship_place('J', 4, 'X')

    def test_ship_placed8(self):
        board = Board(8)
        assert True == board.ship_place('v', 4, 'D')

    def test_ship_placed9(self):
        board = Board(8)
        assert False == board.ship_place('v', 8, 'H')

    def test_shots_fired1(self):
        board = Board(8)
        board.ship_place('h', 1, 'D')
        assert True == board.shot_fired(1, 'D')

    def test_shots_fired2(self):
        board = Board(8)
        board.ship_place('v', 2, 'F')
        assert True == board.shot_fired(3, 'F')

    def test_shots_fired3(self):
        board = Board(8)
        board.ship_place('h', 4, 'C')
        assert False == board.shot_fired(1, 'C')

    def test_shots_fired4(self):
        board = Board(8)
        board.ship_place('v', 2, 'C')
        assert False == board.shot_fired(8, 'C')

    def test_input_validation(self):
        board = Board(8)
        assert True == board.input_validation(1, 'B')
        assert False == board.input_validation(1, 'X')



if __name__ == '__main__':
    unittest.main()
