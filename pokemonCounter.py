import time
from ctypes import windll

dc = windll.user32.GetDC(0)
#white = 16777215
white = 16711422
gray = 3355443
gray_coords = (818, 922)
#gray_coords = (500, 510)
pokemons = {"purrloin": ((712, 900), (797, 900), (876, 900)), "gyarados": "todo"}


def main():
    print("Budget Pokémon Counter script by Thorasine has started!")
    # EDIT THE POKEMON NAME BELOW
    pokemon = "purrloin"
    while True:
        if pixel_checks(pokemon):
            encounter = update_counter()
            print(pokemon + " encounter: " + str(encounter))
            while pixel_checks(pokemon):
                # even without sleep it doesnt hug the cpu, but better safe than sorry
                time.sleep(2.0)
        time.sleep(0.1)


def pixel_checks(pokemon):
    if get_pixel(gray_coords[0], gray_coords[1]) != gray:
        return False
    pokecoords = pokemons[pokemon]
    for i in range(len(pokecoords)):
        if get_pixel(pokecoords[i][0], pokecoords[i][1]) != white:
            return False

    return True


def get_pixel(x, y):
    return windll.gdi32.GetPixel(dc, x, y)


def update_counter():
    try:
        f = open("counter.txt", 'r')
        c = int(f.readline())
        f.close()
        f = open("counter.txt", "w")
        f.write(str(c + 1))
        f.close()
        return c + 1
    except IOError:
        f = open("counter.txt", "w")
        f.write(str(1))
        f.close()
        return 1


def test():
    update_counter()
    print(get_pixel(500, 510))


if __name__ == "__main__":
    main()
