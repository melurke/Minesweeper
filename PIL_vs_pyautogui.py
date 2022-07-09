from PIL import Image

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

def rgb_of_pixel(img, x, y):
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

x_pos = [69, 97, 125, 153, 181, 209, 237, 265, 293, 321, 349, 377, 405, 433, 461, 489, 517, 545, 573, 601, 629, 657, 685, 713, 741, 769, 797, 825, 853, 881]
y_pos = [233, 261, 289, 317, 345, 373, 401, 429, 457, 485, 513, 541, 569, 597, 625, 653]

path = "field.png"
field = ""

for y in y_pos:
    print(str(((y_pos.index(y))/len(y_pos))*100) + "%")
    for x in x_pos:
        image = Image.open(path).convert('RGB')
        rgb = rgb_of_pixel(image, x, y)
        field += rgb

for i in range(0, 16):
        print(field[(30*i):(30*i+29)])
