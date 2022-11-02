import random
import tkinter as tk
from cell import Cell
from universe import Universe
import copy
from time import sleep


class Window:
    def __init__(self, c: tk.Canvas, n: int, m: int, width, height, matrix: list[list[int, Cell]]):
        self.c = c
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.matrix = matrix.matrix

        self.block_h = height / n
        self.block_w = width / m

    def draw(self):
        y = 0
        self.c.delete('all')
        for i in range(1, len(self.matrix)-1):
            x = 0
            for j in range(1, len(self.matrix[i])-1):
                # self.c.clea
                self.c.create_rectangle(
                    x,
                    y,
                    x + self.block_w,
                    y + self.block_h,
                    fill=(self.matrix[i][j].color if self.matrix[i][j] != 0 else 'WHITE'),
                    outline='GREY')
                x += self.block_w

            y += self.block_h

        mat_copy = [i.copy() for i in self.matrix]
        mat = [i.copy() for i in self.matrix]
        mat_copy = copy.deepcopy(self.matrix)

        for i in range(1, 33):
            for j in range(1, 33):
                nn = 0
                difs = [-1, 0, 1]
                for di in difs:
                    for dj in difs:
                        if di != 0 or dj != 0:
                            if type(mat_copy[i + di][j + dj]) == Cell:
                                nn += 1

                if mat_copy[i][j] == 0:
                    if nn == 3:
                        mat[i][j] = 1
                else:
                    if nn != 3 and nn != 2:
                        mat[i][j] = 0
                    else:
                        mat[i][j] = 1
        universe = Universe(mat)

        self.matrix = universe.matrix

        self.c.after(300, self.draw)

