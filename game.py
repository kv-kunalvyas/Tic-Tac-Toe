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
player_1 = player.Player(human=True, mark='X')      # human player
player_2 = player.Player(human=False, mark='O')      # computer

# start the game and don't stop until its over
print 'Choose a pair of numbers separated by space and press return.'
print 'Your symbol =', player_1.mark
print 'Opponent\'s symbol =', player_2.mark
while True:
    # Human's move:
    if '*' in [item for sublist in grid.state for item in sublist]:
        # points are in row, column format
        # update marks the user's move on the board
        if player_1.human is False:
            grid.update(player_1, player_1.auto_move(grid.state, player_2))
        else:
            grid.update(player_1, player_1.human_move(grid))

        # check if player 1 won
        if player_1.check_if_over(grid.state) is True:
            # print success message and exit
            grid.print_board()
            print player_1.mark, '= Player 1 Wins'
            sys.exit(0)
        else:
            # print board after every move if the game isn't over
            grid.print_board()

        # print a divider to differentiate between human's and computer's moves
        print '.' * board_size * 2

    # Player 2's Move:
    if '*' in [item for sublist in grid.state for item in sublist]:
        # update the matrix with player_2's move
        if player_2.human is False:
            grid.update(player_2, player_2.auto_move(grid.state, player_1))
        else:
            grid.update(player_2, player_2.human_move(grid))
        # check if player 2 won
        if player_2.check_if_over(grid.state) is True:
            # print success message and exit
            grid.print_board()
            print player_2.mark, '= Player 2 Wins'
            sys.exit(0)
        else:
            # print board after every move
            grid.print_board()
            print '-Next Move-'

    else:
        # Match drawn if no more moves are possible
        print 'Match Drawn!'
        sys.exit(0)

