from gameplayer import Player

# main method for the program to execute
if __name__ == '__main__':

    # enter players name
    p1_name = input("Enter Player 1 Name: ")
    p1 = Player(p1_name)

    # while the condition is true
    while True:
        p1_ship_d = input("Enter Ship Direction: ")
        p1_ship_r = input("Enter Ship Row Index: ")
        p1_ship_c = input("Enter Ship Column Index: ")

        # checks if the inputs by player are valid or not
        if p1.input_validation(p1_ship_d, p1_ship_r, p1_ship_c):
            if p1.player_ship_placing(p1_ship_d, p1_ship_r, p1_ship_c):
                break
        else:
            print('Kindly Enter Valid values.!')

    # enter player 2 name
    p2_name = input("Enter Player 2 Name: ")
    p2 = Player(p2_name)

    # checks if the condition is true
    while True:
        p2_ship_d = input("Enter Ship Direction: ")
        p2_ship_r = input("Enter Ship Row Index: ")
        p2_ship_c = input("Enter Ship Column Index: ")

        # breaks the loop in case of invalid user inputs
        if p2.input_validation(p2_ship_d, p2_ship_r, p2_ship_c):
            if p2.player_ship_placing(p2_ship_d, p2_ship_r, p2_ship_c):
                break
        else:
            print('Kindly Enter Valid values.!')

    # checks if Player ship is sinked or not
    while not p2.is_sink():

        # attack rounds for each player
        p1_attack_row = input(p1_name + " Enter Attack Row Index: ")
        p1_attack_col = input(p1_name + " Enter Attack Column Index: ")
        p1.player_shots_fired(p2.board, p1_attack_row, p1_attack_col)

        # checks if player 1 has sinked the ship or not after his turn
        if p1.is_sink():
            break

        # attack round for second player
        p2_attack_row = input(p2_name + " Enter Attack Row Index: ")
        p2_attack_col = input(p2_name + " Enter Attack Column Index: ")
        p2.player_shots_fired(p1.board, p2_attack_row, p2_attack_col)