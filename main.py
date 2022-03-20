from tkinter.constants import W
import colors
import random
from tkinter import Button, Canvas, Label, ttk
from tkinter import Tk
from tkinter import StringVar
from tkinter import Frame


window = Tk()
window.title("Morris' Sorting Algorithims Visualizer")
window.maxsize(1000, 700)
window.config(bg=colors.WHITE)

algorithm_name = StringVar()
algo_list = ["Bubble Sort", "Merge Sort"]

speed_name = StringVar()
speed_list = ["Fast", "Medium", "Slow"]

data = []


def draw_data(data, color_array):
    pass


def generate():
    pass


def set_speed():
    pass


def sort():
    pass


# UI HERE #
UI_frame = Frame(window, width=900, height=300, bg=colors.WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Select Algo #
l1 = Label(UI_frame, text="Algorithim: ", bg=colors.WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu.current(0)

# dropdown to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg=colors.WHITE)
l2.grid(row=1, column=10, padx=10, pady=5)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)


# sort button

b1 = Button(UI_frame, text="Sort", command=sort, bg=colors.LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=colors.LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# Canvas to draw array

canvas = Canvas(window, width=800, height=400, bg=colors.WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
