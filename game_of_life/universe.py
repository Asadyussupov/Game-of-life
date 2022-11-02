from cell import Cell
from random import randint
from matrix import matrix


class Universe:
    colors = [(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(100000)]

    def __init__(self, matrix):
        self.matrix = matrix
        for i in range(1, 34):
            for j in range(1, 34):
                cell = matrix[i][j]
                if cell == 1:
                    color = self.colors.pop()
                    self.matrix[i][j] = Cell(i, j, color)

                    self.explore(i, j, color)

    def explore(self, i, j, color):
        difs = [-1, 0, 1]

        for di in difs:
            for dj in difs:
                if di != 0 or dj != 0:
                    if self.matrix[i+di][j+dj] == 1:
                        self.matrix[i+di][j+dj] = Cell(i+di, j+dj, color)
                        self.explore(i+di, j+dj, color)
                    elif type(self.matrix[i+di][j+dj]) == Cell:
                        self.matrix[i + di][j + dj] = Cell(i + di, j + dj, self.matrix[i+di][j+dj].color)