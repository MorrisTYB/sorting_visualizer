import time

DARK_GRAY = "#65696B"
LIGHT_GRAY = "#C4C5BF"
BLUE = "#0CA8F6"
DARK_BLUE = "#4204CC"
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#F22810"
YELLOW = "#F7E806"
PINK = "#F50BED"
LIGHT_GREEN = "#05F50E"
PURPLE = "#BF01FB"


def bubble_sort(data, draw_data, time_tick):
    size = len(data)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1], = (
                    data[j + 1],
                    data[j],
                )
                draw_data(
                    data,
                    [
                        YELLOW if x == j or x == j + 1 else BLUE
                        for x in range(len(data))
                    ],
                )
                time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])
