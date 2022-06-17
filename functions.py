import win32api
import time
import win32con

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

def leftClick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def rightClick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def scan_field(img, x_pos, y_pos, known, empties, ones, twos, threes, fours, fives, sixes, sevens, eights, new_fields):
    empty_field = False
    empty_fields = []
    for f in new_fields:
        if color(img, f[0], f[1]) == "0":
            empty_field = True
            empty_fields.append(f)
    if empty_field:
        for C in empty_fields:
            n = neighbors(C[0], x_pos, C[1], y_pos)
            for N in n:
                if not N in known:
                    col = color(img, N[0], N[1])
                    if col == "0":
                        empties.append(N)
                        empty_fields.append(N)
                    elif col == "1":
                        ones.append(N)
                    elif col == "2":
                        twos.append(N)
                    elif col == "3":
                        threes.append(N)
                    elif col == "4":
                        fours.append(N)
                    elif col == "5":
                        fives.append(N)
                    elif col == "6":
                        sixes.append(N)
                    elif col == "7":
                        sevens.append(N)
                    elif col == "8":
                        eights.append(N)
                    known.append(N)

def color(img, x, y):
    col = img.getpixel((x, y))
    col_2 = img.getpixel((x, y+1))
    if img.getpixel((x-12, y-12)) == unknown:
        return "/"
    elif col[2] == 255:
        return "1"
    elif col[0] == 189:
        return "0"
    elif col_2 == two:
        return "2"
    elif col_2[0] == 255:
        return "3"
    elif img.getpixel((x+2, y)) == four:
        return "4"
    elif col_2 == five:
        return "5"
    elif col_2 == six:
        return "6"
    elif img.getpixel((x, y+5)) == seven:
        return "7"
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
    
def flags(neighbors, num_of_neighbors, known, flags):
    empty_n = []
    num_of_empties = 0

    for N in neighbors:
        if not N in known:
            num_of_empties += 1
            empty_n.append(N)
        elif N in flags:
            num_of_empties += 1
    if num_of_empties == num_of_neighbors:
        for C in empty_n:
            rightClick(C[0], C[1])
        return [empty_n, True]
    else:
        return [[], False]

def no_mines(neighbors, known, flags, num_of_neighbors):
    num_of_flags = 0
    for n in neighbors:
        if n in flags:
            num_of_flags += 1
    if num_of_flags == num_of_neighbors:
        num_of_empty_neighbors = 0
        empty_neighbors = []
        for n in neighbors:
            if not n in known:
                num_of_empty_neighbors += 1
                empty_neighbors.append(n)
                leftClick(n[0], n[1])
        return [empty_neighbors, True]
    return [[], False]

def type(x, y, known, ones, twos, threes, fours, fives, sixes, sevens, eights, empties, flags):
    pos = (x, y)
    if not pos in known:
        T = "/"
    elif pos in empties:
        T = "0"
    elif pos in flags:
        T = "!"
    elif pos in ones:
        T = "1"
    elif pos in twos:
        T = "2"
    elif pos in threes:
        T = "3"
    elif pos in fours:
        T = "4"
    elif pos in fives:
        T = "5"
    elif pos in sixes:
        T = "6"
    elif pos in sevens:
        T = "7"
    elif pos in eights:
        T = "8"
    return T

def guess(x_pos, y_pos, known, empties, flags, ones, twos, threes, fours, fives, sixes, sevens, eights):
    probabilities = [[1, 0]] * 480

    for C in known:
        probabilities[(y_pos.index(C[1])*30+x_pos.index(C[0]))] = [0, 0]
        if not C in empties and not C in flags:
            num_of_flags = int(type(C[0], C[1], known, ones, twos, threes, fours, fives, sixes, sevens, eights, empties, flags))
            n = neighbors(C[0], x_pos, C[1], y_pos)
            empty_n = []
            num_of_free_neighbors = 0
            num_of_used_flags = 0
            for N in n:
                if N in empties:
                    empty_n.append(N)
                    num_of_free_neighbors += 1
                elif N in flags:
                    num_of_used_flags += 1
            num_of_free_flags = num_of_flags - num_of_used_flags
            try:
                p = num_of_free_flags / num_of_free_neighbors
            except ZeroDivisionError:
                p = 0
            for N in empty_n:
                x_coord = x_pos.index(N[0])
                y_coord = y_pos.index(N[1])
                if p != 0:
                    probabilities[y_coord*30+x_coord][0] += p
                    probabilities[y_coord*30+x_coord][1] += 1
    new_probabilities = []
    for b in probabilities.copy():
        try:
            c = b[0] / b[1]
        except ZeroDivisionError:
            c = 1
        new_probabilities.append(c)
    min_index = new_probabilities.index(min(new_probabilities))
    x_index = min_index % 30
    y_index = int((min_index-x_index)/16)
    try:
        coords = (x_pos[x_index], y_pos[y_index])
        print(new_probabilities)
        print(f"{x_index}, {y_index}: {new_probabilities[min_index]}")
        return coords
    except:
        return
