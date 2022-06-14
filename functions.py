import pyautogui

unknown = (255, 255, 255)
empty = (189, 189, 189)
one = (0, 0, 255)
two = (0, 123, 0)
three = (255, 0, 0)
four = (0, 0, 123)
five = (123, 0, 0)
six = (0, 123, 123)
seven = (0, 0, 0)
eight = (123, 123, 123)

def scan_field(x_pos, y_pos, known, empties, ones, twos, threes, fours, fives, sixes, sevens, eights, flags, new_fields):
    field = [""] * 16
    empty_field = False
    for f in new_fields:
        col = color(f[0], f[1])
        if col == "/":
            empties.append(f)
    if empty_field:
        for y in y_pos:
            for x in x_pos:
                if not (x_pos.index(x)+1, y_pos.index(y)+1) in known:
                    col = color(x, y)
                    if col == "/":
                        empties.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "1":
                        ones.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "2":
                        twos.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "3":
                        threes.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "4":
                        fours.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "5":
                        fives.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "6":
                        sixes.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "7":
                        sevens.append((x_pos.index(x)+1, y_pos.index(y)+1))
                    elif col == "8":
                        eights.append((x_pos.index(x)+1, y_pos.index(y)+1))
                else:
                    if (x_pos.index(x)+1, y_pos.index(y)+1) in flags:
                        col = "!"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in ones:
                        col = "1"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in twos:
                        col = "2"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in threes:
                        col = "3"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in fours:
                        col = "4"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in fives:
                        col = "5"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in sixes:
                        col = "6"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in sevens:
                        col = "7"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in eights:
                        col = "8"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in empties:
                        col = "/"
                field[y_pos.index(y)] += col
    else:
        for y in y_pos:
            for x in x_pos:
                if (x_pos.index(x)+1, y_pos.index(y)+1) in known:
                    if (x_pos.index(x)+1, y_pos.index(y)+1) in flags:
                        col = "!"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in ones:
                        col = "1"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in twos:
                        col = "2"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in threes:
                        col = "3"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in fours:
                        col = "4"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in fives:
                        col = "5"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in sixes:
                        col = "6"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in sevens:
                        col = "7"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in eights:
                        col = "8"
                    elif (x_pos.index(x)+1, y_pos.index(y)+1) in empties:
                        col = "/"
                else:
                    col = "0"
                field[y_pos.index(y)] += col
    return field

def color(x, y):
    col = pyautogui.pixel(x, y)
    col_2 = pyautogui.pixel(x, y+1)
    if col == empty:
        if pyautogui.pixel(x-12, y-12) == unknown:
            return "0"
        else:
            return "/"
    elif col == one:
        return "1"
    elif col_2 == two:
        return "2"
    elif col_2 == three:
        return "3"
    elif pyautogui.pixel(x+2, y) == four:
        return "4"
    elif col_2 == five:
        return "5"
    elif pyautogui.pixel(x-1, y) == six:
        return "6"
    elif pyautogui.pixel(x, y+5) == seven:
        return "7"
    elif col == eight:
        return "8"
    return "!"

def neighbors(x, x_pos, y, y_pos):
    n = []
    for X in range(0, 3):
        for Y in range(0, 3):
            if not X == Y == 1:
                x_ = (X-1)*28 + x
                y_ = (Y-1)*28 + y
                if x_ in x_pos and y_ in y_pos:
                    n.append((x_, y_))
    return n
    
def flags(neighbors, num_of_neighbors, x_pos, y_pos, known, flags):
    empty_n = []
    num_of_empties = 0

    for N in neighbors:
        coords = (x_pos.index(N[0])+1, y_pos.index(N[1])+1)
        if not coords in known:
            num_of_empties += 1
            empty_n.append((coords[0]-1, coords[1]-1))
        elif coords in flags:
            num_of_empties += 1
    if num_of_empties == num_of_neighbors:
        return [empty_n, True]
    else:
        return [empty_n, False]

def no_mines(neighbors, x_pos, y_pos, known, flags, num_of_neighbors):
    num_of_flags = 0
    for n in neighbors:
        coords = (x_pos.index(n[0])+1, y_pos.index(n[1])+1)
        if coords in flags:
            num_of_flags += 1
    if num_of_flags == num_of_neighbors:
        num_of_empty_neighbors = 0
        empty_neighbors = []
        for n in neighbors:
            coords = (x_pos.index(n[0])+1, y_pos.index(n[1])+1)
            if not coords in known:
                num_of_empty_neighbors += 1
                empty_neighbors.append(n)
        return [empty_neighbors, True]
    return [[], False]
