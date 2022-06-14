import pyautogui
import time
import functions as f

x_pos = [69, 97, 125, 153, 181, 209, 237, 265, 293, 321, 349, 377, 405, 433, 461, 489, 517, 545, 573, 601, 629, 657, 685, 713, 741, 769, 797, 825, 853, 881]
y_pos = [233, 261, 289, 317, 345, 373, 401, 429, 457, 485, 513, 541, 569, 597, 625, 653]
flags = []
bombs = []
ones = []
twos = []
threes = []
fours = []
fives = []
sixes = []
sevens = []
eights = []
empties = []
known = []
new_fields = []
clicked = True
first_round = True

while True:
    pyautogui.moveTo(1000, 500)
    field = [""] * 16
    for pi in new_fields:
        col = f.color(pi[0], pi[1])
        if col == "/":
            empties.append(pi)
        elif col == "1":
            ones.append(pi)
        elif col == "2":
            twos.append(pi)
        elif col == "3":
            threes.append(pi)
        elif col == "4":
            fours.append(pi)
        elif col == "5":
            fives.append(pi)
        elif col == "6":
            sixes.append(pi)
        elif col == "7":
            sevens.append(pi)
        elif col == "8":
            eights.append(pi)
        known.append(pi)
    if not first_round:
        if clicked:
            field = f.scan_field(x_pos, y_pos, known, empties, ones, twos, threes, fours, fives, sixes, sevens, eights, flags, new_fields)
        else:
            for y in range(0, 16):
                for x in range(0, 30):
                    if (y+1, x+1) in flags:
                        field[y] += "!"
                    elif (y+1, x+1) in ones:
                        field[y] += "1"
                    elif (y+1, x+1) in twos:
                        field[y] += "2"
                    elif (y+1, x+1) in threes:
                        field[y] += "3"
                    elif (y+1, x+1) in fours:
                        field[y] += "4"
                    elif (y+1, x+1) in fives:
                        field[y] += "5"
                    elif (y+1, x+1) in sixes:
                        field[y] += "6"
                    elif (y+1, x+1) in sevens:
                        field[y] += "7"
                    elif (y+1, x+1) in eights:
                        field[y] += "8"
                    elif (y+1, x+1) in empties:
                        field[y] += "/"
                    else:
                        field[y] += "0"
    else:
        for y in y_pos:
            for x in x_pos:
                if not (x_pos.index(x)+1, y_pos.index(y)+1) in known:
                    col = f.color(x, y)
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
    for row in field:
        print(row)
    print("")
    print("")
    clicked = False

    known = flags + ones + twos + threes + fours + sixes + sevens + eights + empties
    known = list(dict.fromkeys(known))
    known.sort()

    for C in known.copy():
        pass_field = False
        num_of_neighbors = 0
        if C in flags or C in empties:
            pass_field = True
        if not pass_field:
            if C in ones:
                num_of_neighbors = 1
            elif C in twos:
                num_of_neighbors = 2
            elif C in threes:
                num_of_neighbors = 3
            elif C in fours:
                num_of_neighbors = 4
            elif C in fives:
                num_of_neighbors = 5
            elif C in sixes:
                num_of_neighbors = 6
            elif C in sevens:
                num_of_neighbors = 7
            elif C in eights:
                num_of_neighbors = 8
            
            x_coord = x_pos[C[0]-1]
            y_coord = y_pos[C[1]-1]

            n = f.flags(f.neighbors(x_coord, x_pos, y_coord, y_pos), num_of_neighbors, x_pos, y_pos, known, flags)
            
            if n[1]:
                for E in n[0]:
                    x_coord = x_pos[E[0]]
                    y_coord = y_pos[E[1]]
                    pyautogui.rightClick(x_coord, y_coord)
                    flags.append((E[0]+1, E[1]+1))
                    known.append((E[0]+1, E[1]+1))

    new_fields = []

    for C in known.copy():
        pass_field = False
        num_of_neighbors = 0

        if C in flags or C in empties:
            pass_field = True
        if not pass_field:
            if C in ones:
                num_of_neighbors = 1
            elif C in twos:
                num_of_neighbors = 2
            elif C in threes:
                num_of_neighbors = 3
            elif C in fours:
                num_of_neighbors = 4
            elif C in fives:
                num_of_neighbors = 5
            elif C in sixes:
                num_of_neighbors = 6
            elif C in sevens:
                num_of_neighbors = 7
            elif C in eights:
                num_of_neighbors = 8

            x_coord = x_pos[C[0]-1]
            y_coord = y_pos[C[1]-1]

            n = f.no_mines(f.neighbors(x_coord, x_pos, y_coord, y_pos), x_pos, y_pos, known, flags, num_of_neighbors)

            if n[1]:
                for E in n[0]:
                    pyautogui.leftClick(E[0], E[1])
                    new_fields.append((x_pos.index(E[0])+1, y_pos.index(E[1])+1))
                    clicked = True
    if pyautogui.locateOnScreen("smiley.png") != None:
        break
    time.sleep(1)
    first_round = False
