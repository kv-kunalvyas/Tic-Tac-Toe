import random


class Player(object):
    """
    Defines the class for the player with methods to move and check if won
    """
    def __init__(self, mark):
        # mark is the symbol used by players (i.e a nought(O) or a cross(X))
        self.mark = mark

    @property
    def get_mark(self):
        # type: () -> string
        return self.mark

    def auto_move(self, matrix, opponent):
        """
        Logic for next move made by the computer
        :param matrix: nXn matrix of board (list of lists)
        :param opponent: Player object of the opponent
        :return: row and column value of suggested move
        """

        # check if we can win in the next move
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == '*':
                    # replace an unmoved spot with move and check if it leads to
                    # winning the game
                    matrix[i][j] = self.mark
                    if self.check_if_over(matrix) is True:
                        return i, j
                    # replacing the mark with '*'
                    matrix[i][j] = '*'

        # check if opponent will win in the next move
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == '*':
                    # replace an unmoved spot with opponent's possible move
                    # and check if it leads to winning the game and prevent it
                    matrix[i][j] = opponent.get_mark
                    if opponent.check_if_over(matrix) is True:
                        return i, j
                    matrix[i][j] = '*'

        # otherwise, move on any random spot from what is available
        available_spots = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == '*':
                    # collect all available moves in a list
                    available_spots.append([i, j])
                    matrix[i][j] = '*'

        # select a random point out of the available to make a move
        return random.choice(available_spots)

    @staticmethod
    def human_move(current_grid):
        """
        Allows human to make a move
        :param current_grid:
        :return: row and column of move made by human
        """
        while True:
            value = raw_input()
            try:
                row, column = value.split()
                row = int(row)
                column = int(column)
            except ValueError:
                # if value is invalid, it displays example of valid input and lets
                # player try again
                print 'For Example: Type "0 ' + \
                    str(range(current_grid.get_size)[-1]) + \
                    '" to move on top right corner'
                continue

            # Checks further if move is valid and returns the row and column
            if row in range(current_grid.get_size) and column in range(current_grid.get_size):
                if current_grid.get_matrix[row][column] == '*':
                    return tuple([row, column])
                else:
                    print 'Move Not Allowed: You can only make a move at a new position, please try again'
            else:
                print 'Illegal Input: Both row and column should be from values', \
                    range(current_grid.get_size), 'Try again'

    def check_if_over(self, matrix):
        """
        Checks if the game is over and displays message accordingly

        :param matrix: matrix of the grid/board as a list of lists
        :return: True if an n-in-a-row combination is found in a nXn matrix
        """

        def check_win(items):
            """
            Takes in list of items along a diagonal/axis
            :param items: list of items in a row
            :return: True if player wins
            """
            return set(items) == set(self.get_mark)

        # check horizontals
        for row in matrix:
            # check if the row has same marks/symbols. If so, the player has won
            if check_win(row) is True:
                return True
            else:
                pass

        # check verticals
        for column in range(len(matrix)):
            # collect all vertical points in the matrix
            vertical_moves = [item[column] for item in matrix]
            # check if the player has won or not
            if check_win(vertical_moves) is True:
                return True
            else:
                pass

        # check diagonals
        fwd_diagonal, bwd_diagonal = [], []
        for row in range(len(matrix)):
            # add points at diagonals to the lists
            fwd_diagonal.append(matrix[row][row])
            bwd_diagonal.append(matrix[row][len(matrix) - row - 1])
        # check if a winning combination is found
        if check_win(fwd_diagonal) is True or check_win(bwd_diagonal) is True:
            return True
        else:
            return False
