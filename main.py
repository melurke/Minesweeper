import pyautogui
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
end_game = False

while True:
    pyautogui.moveTo(1000, 500)
    field = [""] * 16
    for pi in new_fields:
        col = f.color(pi[0], pi[1])
        if col == "0":
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
            print("Get known fields:")
            for y in y_pos:
                print(str(((y_pos.index(y))/len(y_pos))*100) + "%")
                for x in x_pos:
                    if (x, y) in flags:
                        field[y] += "!"
                    elif (x, y) in ones:
                        field[y] += "1"
                    elif (x, y) in twos:
                        field[y] += "2"
                    elif (x, y) in threes:
                        field[y] += "3"
                    elif (x, y) in fours:
                        field[y] += "4"
                    elif (x, y) in fives:
                        field[y] += "5"
                    elif (x, y) in sixes:
                        field[y] += "6"
                    elif (x, y) in sevens:
                        field[y] += "7"
                    elif (x, y) in eights:
                        field[y] += "8"
                    elif (x, y) in empties:
                        field[y] += "0"
                    else:
                        field[y] += "/"
    else:
        print("Scan full field:")
        for y in y_pos:
            print(str(((y_pos.index(y))/len(y_pos))*100) + "%")
            for x in x_pos:
                if not (x, y) in known:
                    col = f.color(x, y)
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
                field[y_pos.index(y)] += col
    for row in field:
        print(row)
    known_fields = known.copy()
    print("")
    print("")

    clicked = False
    known = flags + ones + twos + threes + fours + fives + sixes + sevens + eights + empties
    known = list(dict.fromkeys(known))
    known.sort()

    for C in known.copy():
        num_of_neighbors = 0
        if not C in flags and not C in empties:
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

            n = f.flags(f.neighbors(C[0], x_pos, C[1], y_pos), num_of_neighbors, known, flags)
            
            if n[1]:
                flags += n[0]
                known += n[0]

    new_fields = []

    for C in known.copy():
        num_of_neighbors = 0

        if not C in flags and not C in empties:
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

            n = f.no_mines(f.neighbors(C[0], x_pos, C[1], y_pos), known, flags, num_of_neighbors)

            new_fields += n[0]
            if n[1]:
                clicked = True

    if known == known_fields:
        print("Taking guess:")
        guess = f.guess(x_pos, y_pos, known, empties, flags, ones, twos, threes, fours, fives, sixes, sevens, eights)
        pyautogui.click(guess[0], guess[1])
        break
    if pyautogui.locateOnScreen("smiley.png") != None:
        break
    first_round = False
print("")
print("The game ended!")
