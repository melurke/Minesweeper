import pyautogui
import functions as f
import keyboard
import time

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
no_more_moves = False

while not keyboard.is_pressed('k'):
    f.leftClick(474, 174)
    f.leftClick(459, 430)
    time.sleep(0.2)
    while not keyboard.is_pressed('l'): # Press l to generate a new starting position / Press and hold k and then press l to use the given starting position
        time.sleep(0.05)

while True:
    img = pyautogui.screenshot("field.png")
    pyautogui.moveTo(1000, 500)
    for pi in new_fields:
        col = f.color(img, pi[0], pi[1])
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
            f.scan_field(img, x_pos, y_pos, known, empties, ones, twos, threes, fours, fives, sixes, sevens, eights, new_fields)
    else:
        for y in y_pos:
            for x in x_pos:
                if not (x, y) in known:
                    col = f.color(img, x, y)
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
    known_fields = known.copy()

    clicked = False
    known = flags + ones + twos + threes + fours + fives + sixes + sevens + eights + empties
    known = list(dict.fromkeys(known))
    known.sort()

    for C in known.copy():
        num_of_neighbors = 0
        if not C in flags and not C in empties:
            num_of_neighbors = int(f.type(C[0], C[1], known, ones, twos, threes, fours, fives, sixes, sevens, eights, empties, flags))
            n = f.flags(f.neighbors(C[0], x_pos, C[1], y_pos), num_of_neighbors, known, flags)

            if n[1]:
                flags += n[0]
                known += n[0]

    new_fields = []

    for C in known.copy():
        num_of_neighbors = 0

        if not C in flags and not C in empties:
            num_of_neighbors = int(f.type(C[0], C[1], known, ones, twos, threes, fours, fives, sixes, sevens, eights, empties, flags))
            n = f.no_mines(f.neighbors(C[0], x_pos, C[1], y_pos), known, flags, num_of_neighbors)

            new_fields += n[0]
            if n[1]:
                clicked = True

    if known == known_fields  and no_more_moves:
        print("Taking guess:")
        guess = f.guess(x_pos, y_pos, known, empties, flags, ones, twos, threes, fours, fives, sixes, sevens, eights)
        try:
            f.leftClick(guess[0], guess[1])
        except:
            pass
        break
    elif known == known_fields:
        no_more_moves = True
    if keyboard.is_pressed('q'):
        break
    first_round = False
f.leftClick(1000, 500)
print("")
print("The game ended!")
