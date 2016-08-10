# Author: Kunal Vyas


class Board(object):
    """
    Board class: creates and maintains the tic-tac-toe board
    """

    def __init__(self, size):
        self.state = []
        self.size = size
        # Create a square matrix of '*'s
        for x in range(self.size):
            self.state.append(list())
            for y in range(self.size):
                self.state[x].append('*')

    @property
    def get_size(self):
        return self.size

    @property
    def get_matrix(self):
        # type: () -> list of lists
        return self.state

    def update(self, player_number, point):
        """
        Takes in player object and tuple of coordinates and updates the move on
        the board
        :return: prints the current grid on the console
        """
        self.state[point[0]][point[1]] = player_number.get_mark

    def print_board(self):
        """
        Prints the board on the console
        :return:
        """
        for row in self.state:
            for item in row:
                print item,
            print
