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


def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end + 1):
        if p > mid:
            tempArray.append(data[q])
            q += 1
        elif q > end:
            tempArray.append(data[p])
            p += 1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p += 1
        else:
            tempArray.append(data[q])
            q += 1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1


def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid + 1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(
            data,
            [
                PURPLE
                if x >= start and x < mid
                else YELLOW
                if x == mid
                else DARK_BLUE
                if x > mid and x <= end
                else BLUE
                for x in range(len(data))
            ],
        )
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
