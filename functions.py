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
        if color(f[0], f[1]) == "0":
            empty_field = True
    if empty_field:
        print("Scan full field:")
        for y in y_pos:
            print(str(((y_pos.index(y))/len(y_pos))*100) + "%")
            for x in x_pos:
                if not (x, y) in known:
                    col = color(x, y)
                    if col == "0":
                        empties.append((x, y))
                    elif col == "1":
                        ones.append((x, y))
                    elif col == "2":
                        twos.append((x, y))
                    elif col == "3":
                        threes.append((x, y))
                    elif col == "4":
                        fours.append((x, y))
                    elif col == "5":
                        fives.append((x, y))
                    elif col == "6":
                        sixes.append((x, y))
                    elif col == "7":
                        sevens.append((x, y))
                    elif col == "8":
                        eights.append((x, y))
                else:
                    if (x, y) in flags:
                        col = "!"
                    elif (x, y) in ones:
                        col = "1"
                    elif (x, y) in twos:
                        col = "2"
                    elif (x, y) in threes:
                        col = "3"
                    elif (x, y) in fours:
                        col = "4"
                    elif (x, y) in fives:
                        col = "5"
                    elif (x, y) in sixes:
                        col = "6"
                    elif (x, y) in sevens:
                        col = "7"
                    elif (x, y) in eights:
                        col = "8"
                    elif (x, y) in empties:
                        col = "0"
                    else:
                        col = "/"
                field[y_pos.index(y)] += col
    else:
        print("Scan neighbors:")
        for y in y_pos:
            print(str(((y_pos.index(y))/len(y_pos))*100) + "%")
            for x in x_pos:
                if (x, y) in known:
                    if (x, y) in flags:
                        col = "!"
                    elif (x, y) in ones:
                        col = "1"
                    elif (x, y) in twos:
                        col = "2"
                    elif (x, y) in threes:
                        col = "3"
                    elif (x, y) in fours:
                        col = "4"
                    elif (x, y) in fives:
                        col = "5"
                    elif (x, y) in sixes:
                        col = "6"
                    elif (x, y) in sevens:
                        col = "7"
                    elif (x, y) in eights:
                        col = "8"
                    elif (x, y) in empties:
                        col = "0"
                else:
                    col = "/"
                field[y_pos.index(y)] += col
    return field

def color(x, y):
    col = pyautogui.pixel(x, y)
    col_2 = pyautogui.pixel(x, y+1)
    if pyautogui.pixel(x-12, y-12) == unknown:
        return "/"
    elif col[2] == 255:
        return "1"
    elif col[0] == 189:
        return "0"
    elif col_2 == two:
        return "2"
    elif col_2[0] == 255:
        return "3"
    elif pyautogui.pixel(x+2, y) == four:
        return "4"
    elif col_2 == five:
        return "5"
    elif col_2 == six:
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
            pyautogui.rightClick(C[0], C[1])
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
                pyautogui.click(n[0], n[1])
        return [empty_neighbors, True]
    return [[], False]

def guess(x_pos, y_pos, known, empties, flags, ones, twos, threes, fours, fives, sixes, sevens, eights):
    probabilities = [[1, 0]] * 480

    for C in known:
        num_of_flags = 0
        if not C in empties and not C in flags:
            if C in ones:
                num_of_flags = 1
            elif C in twos:
                num_of_flags = 2
            elif C in threes:
                num_of_flags = 3
            elif C in fours:
                num_of_flags = 4
            elif C in fives:
                num_of_flags = 5
            elif C in sixes:
                num_of_flags = 6
            elif C in sevens:
                num_of_flags = 7
            elif C in eights:
                num_of_flags = 8
            n = neighbors(C[0], x_pos, C[1], y_pos)
            empty_n = []
            num_of_free_neighbors = 0
            num_of_free_flags = 0
            num_of_used_flags = 0
            for N in n:
                if N in flags:
                    num_of_used_flags += 1
                elif N in empty:
                    num_of_free_neighbors += 1
                    empty_n.append(N)
            print(C)
            print(empty_n)
            num_of_free_flags = num_of_flags - num_of_used_flags
            try:
                p = num_of_free_flags / num_of_free_neighbors
            except ZeroDivisionError:
                p = 20
            # FIXME:
            for N in empty_n:
                x_coord = N[0]
                y_coord = N[1]
                probabilities[y_coord*16+x_coord][0] += p
                probabilities[y_coord*16+x_coord][1] += 1
                print(probabilities[y_coord*16+x_coord])
    new_probabilities = []
    print(probabilities)
    for b in probabilities.copy():
        try:
            c = b[0] / b[1]
        except ZeroDivisionError:
            c = 1
        new_probabilities.append(c)
    print(new_probabilities)
    probabilities = new_probabilities.copy()
    min_index = probabilities.index(min(probabilities))
    x_index = min_index % 16
    y_index = int((min_index-x_index)/16)

    coords = (x_pos[x_index], y_pos[y_index])
    print(probabilities)
    print(x_index, y_index)
    return coords
