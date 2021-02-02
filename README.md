# BattleshipPython

The project is based on Python 3.9

This is a battleship game developed in python using python unit testing and automated build deployment tool CircleCI.

The project is test driven. and uses OOP concepts for development.

The test cases provide almost 95% code coverage.

Using python coverage for reports on unit test cases.
- pip install coverage
- coverage run test.py
-coverage report -m

the game play is divided in 3 classes:
1. gameboard.py - which deals with board objects, ship placing logic and play attack logic. it also handles validations for user input
2. gameplay.py - which deals with player objects, and gameplay for each player. contains methods to define board for each player, ship placement and attack rounds.
3. playbattle.py - contains the main method which starts the game and asks for player name, placing of ships and handles wrong inputs of user.

