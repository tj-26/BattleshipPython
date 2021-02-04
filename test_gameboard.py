from gameboard import Board
from gameplayer import Player
import unittest

class MyTestCase(unittest.TestCase):

    # test the grid board length
    def test_board_grid(self):
        board = Board(8)
        assert 8 == len(board.print_board())

    # test the mapping of user input
    def test_user_map(self):
        board = Board(8)
        assert 7, 0 == board.map_user_input(8, 'A')

    # testing wrong mapping to be false
    def test_user_map2(self):
        board = Board(8)
        assert 7, 0 != board.map_user_input(5, 'A')

    # testing ship placing method function
    def test_ship_placed(self):
        board = Board(8)
        assert True == board.ship_place('h', 1, 'A')
        
    def test_ship_placed2():
        board = Board(8)
        assert False == board.ship_place('K', 1, 'D')

    # testing validations put for testing method function
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
    # testing the attack method logic
    def test_shots_fired1(self):
        board = Board(8)
        board.ship_place('h', 1, 'D')
        assert True == board.shot_fired(1, 'D')

    def test_shots_fired2(self):
        board = Board(8)
        board.ship_place('v', 2, 'F')
        assert True == board.shot_fired(3, 'F')

    # testing the hit or miss logic
    def test_shots_fired3(self):
        board = Board(8)
        board.ship_place('h', 4, 'C')
        assert False == board.shot_fired(1, 'C')

    def test_shots_fired4(self):
        board = Board(8)
        board.ship_place('v', 2, 'C')
        assert False == board.shot_fired(8, 'C')

    # testing the input validation method
    def test_input_validation(self):
        board = Board(8)
        assert True == board.input_validation(1, 'B')
        assert False == board.input_validation(1, 'X')

    # test for player object and his own game board
    def test_player_object(self):
        p1 = Player('Test Player 1')
        assert p1.name == 'Test Player 1'
        assert len(p1.board.print_board()) == 8
        assert p1.counter == 0

    # testing the player ship placing logic
    def test_palyer_ship_place1(self):
        p1 = Player('Test Player 1')
        assert True == p1.player_ship_placing('h', 2, 'A')

    def test_palyer_ship_place2(self):
        p1 = Player('Test Player 1')
        assert False == p1.player_ship_placing('v', 8, 'A')

    # testing player shot fired on other player's board logic
    def test_palyer_shot_fired1(self):

        p1 = Player('Test Player 1')
        p1.player_ship_placing('h', 3, 'A')
        p2 = Player('Test Player 2')
        p2.player_ship_placing('v', 3, 'A')
        assert True == p1.player_shots_fired(p2.board, '3', 'A')
        assert False == p2.player_shots_fired(p1.board, '3', 'G')
        
    # testing player shot fired on other player's board logic for sinking
    def test_palyer_shot_fired2(self):

        p1 = Player('Test Player 1')
        p1.player_ship_placing('h', 3, 'A')
        p2 = Player('Test Player 2')
        p2.player_ship_placing('v', 3, 'A')
        p1.player_shots_fired(p2.board, '3', 'A')
        p1.player_shots_fired(p2.board, '4', 'A')
        p1.player_shots_fired(p2.board, '5', 'A')
        assert True == p1.is_sink()

if __name__ == '__main__':
    unittest.main()

