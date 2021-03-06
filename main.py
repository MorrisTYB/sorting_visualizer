from tkinter.constants import W
import colors
import random
from tkinter import Button, Canvas, Label, ttk
from tkinter import Tk
from tkinter import StringVar
from tkinter import Frame
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort


window = Tk()
window.title("Morris' Sorting Algorithims Visualizer")
window.maxsize(1000, 700)
window.config(bg=colors.DARK_GRAY)

algorithm_name = StringVar()
algo_list = ["Bubble Sort", "Merge Sort"]

speed_name = StringVar()
speed_list = ["Fast", "Medium", "Slow"]

data = []


def draw_data(data, color_array):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 300
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

    window.update_idletasks()


def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    draw_data(data, [colors.BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == "Slow":
        return 0.3

    elif speed_menu.get() == "Medium":
        return 0.1

    else:
        return 0.001


def sort():
    global data
    time_tick = set_speed()

    if algo_menu.get() == "Bubble Sort":
        bubble_sort(data, draw_data, time_tick)

    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, 0, len(data) - 1, draw_data, time_tick)


# UI HERE #
UI_frame = Frame(window, width=900, height=300, bg=colors.DARK_GRAY)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Select Algo #
l1 = Label(UI_frame, text="Algorithim: ", bg=colors.DARK_GRAY)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=10, pady=5, sticky=W)
algo_menu.current(0)

# dropdown to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg=colors.DARK_GRAY)
l2.grid(row=1, column=0, padx=10, pady=5)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)


# sort button

b1 = Button(UI_frame, text="Sort", command=sort, bg=colors.WHITE)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=colors.WHITE)
b3.grid(row=2, column=0, padx=5, pady=5)

# Canvas to draw array

canvas = Canvas(window, width=800, height=400, bg=colors.WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
