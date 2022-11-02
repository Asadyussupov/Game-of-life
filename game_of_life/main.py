import tkinter as tk
from window import Window
from random import randint
from cell import Cell
from matrix import matrix
from universe import Universe
from time import sleep

root = tk.Tk()
root.geometry('640x640')

canvas = tk.Canvas(root, width=640, height=640, background='Blue')
canvas.pack()

universe = Universe(matrix)

# for i in universe.matrix:
#     print(i)

field = Window(canvas, 32, 32, 640, 640, universe)
field.draw()

root.mainloop()
