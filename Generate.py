import random
import numpy as np


class Generate(object):
    # Initialize the nine grid
    def __init__(self, n):
        # int8，int16，int32，int64
        self.martix = np.zeros((9, 9), dtype='i1')
        self.Nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.n = n  # number of be remove

        # Save the dug Sudoku while digging the hole
        self.uniqueMartix = []

    # Building Sudoku
    def build_martix(self):
        while not self.LasVegas(11):
            pass
        self.Generate(self.n)
        return self.martix

    # Las Vegas algorithm generates Sudoku
    def LasVegas(self, counts):
        """
        :param counts: The number of digits generated
        :return:
        """
        while counts:
            # [x, y] Is the table position, that is, the table position is randomly generated
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            # A space in a grid
            if self.martix[row, col] == 0:
                # Random fetch number
                value = random.sample(self.Get_possible(row, col), 1)[0]
                self.martix[row, col] = value
                counts -= 1

        if self.Solve():
            return True
        else:
            return False

    def Solve(self):
        for row in range(9):
            for col in range(9):
                if self.martix[row, col] == 0:
                    possible = self.Get_possible(row, col)  # All the possible numbers
                    for value in possible:
                        self.martix[row, col] = value
                        if self.Solve():
                            return True
                        self.martix[row, col] = 0
                        self.row, self.col = row, col
                    return False
        print(self.martix)
        return True

    # The numbers [1, 9] are arranged randomly
    def Get_possible(self, row, col):
        """
        :param row:
        :param col:
        :return:
        """
        x, y = row // 3, col // 3
        """
        self.martix[row, :]: [row, col]Row of the board
        self.martix[:, col]: [row, col]Col of the board
        """
        rowSet = set(self.martix[row, :])  # [row, col]
        colSet = set(self.martix[:, col])  # [row, col]
        blockSet = set(self.martix[x * 3: x * 3 + 3, y * 3: y * 3 + 3].reshape(9))  # [row, col]

        return self.Nums - rowSet - colSet - blockSet

    # Generate Sudoku questions from Sudoku disks
    def Generate(self, n):
        # level
        self.uniqueMartix = self.martix.copy()

        counts = 0
        while counts < n:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            if self.uniqueMartix[row, col] == 0:
                continue

            if self.IsUnique(row, col):
                self.uniqueMartix[row, col] = 0
                self.martix = self.uniqueMartix.copy()

                counts += 1


    def IsUnique(self, row, col):
        for value in range(1, 10):
            if self.martix[row][col] != value:
                self.martix[row][col] = 0
                if value in self.Get_possible(row, col):
                    self.martix[row][col] = value
                    if self.Solve():
                        return False


                self.martix = self.uniqueMartix.copy()
        return True