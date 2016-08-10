# Author: Kunal Vyas

"""
INSTRUCTIONS, RULES & LIMITATIONS
Human gets to move first
To make a move, type in two digits separated by a space on the console
This version is played as a human against a computer
This works only for square boards, i.e n X n boards
The first player to have n-in-a-row(of a nXn matrix) marks on the matrix wins
"""


import sys
import board
import player

# Set values of some customisable features of the game
board_size = 3                          # board size (n by n)
grid = board.Board(size=board_size)     # initialise the board
player_1 = player.Player(mark='O')      # human player
player_2 = player.Player(mark='X')      # computer

# start the game and don't stop until its over
print 'Choose a pair of numbers separated by space and press return.\n'
while True:
    # Human's move:
    if '*' in [item for sublist in grid.get_matrix for item in sublist]:
        # points are in row, column format
        # update marks the user's move on the board
        grid.update(player_1, player_1.human_move(grid))

        # check if player 1 won
        if player_1.check_if_over(grid.get_matrix) is True:
            # print success message and exit
            grid.print_board()
            print player_1.get_mark, '= Human Wins'
            sys.exit(0)
        else:
            # print board after every move if the game isn't over
            grid.print_board()

        print '.' * board_size * 2

    # Computer's Move:
    if '*' in [item for sublist in grid.get_matrix for item in sublist]:
        # update the matrix with player_2's move
        grid.update(player_2, player_2.auto_move(grid.get_matrix, player_1))

        # check if player 2 won
        if player_2.check_if_over(grid.get_matrix) is True:
            # print success message and exit
            grid.print_board()
            print player_2.get_mark, '= Computer Wins'
            sys.exit(0)
        else:
            # print board after every move
            grid.print_board()
            print '-Next Move-'

    else:
        # Match drawn if no more moves are possible
        print 'Match Drawn!'
        sys.exit(0)

