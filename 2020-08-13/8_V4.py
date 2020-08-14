import curses
import random
from time import sleep


def main(screen):
    point = 0
    x = 1
    y = 1
    wall_x = 0
    wall_x2 = 25
    wall_y2 = 0
    wall_y3 = 25
    main = "d"

    for f in range(1,6):
        dollar_x = random.randint(2, 24)
        dollar_y = random.randint(2, 24)
        screen.addstr(dollar_y, dollar_x, "$")
        # A = chr(screen.inch(dollar_y,dollar_x)))

    for wall_y in range(0, 26):
        screen.addstr(wall_y, wall_x, "#")
        screen.addstr(wall_y, wall_x2, "#")
    for wall_x3 in range(0, 26):
        screen.addstr(wall_y2, wall_x3, "#")
        screen.addstr(wall_y3, wall_x3, "#")

    curses.curs_set(0)
    while point < 5:
        screen.addstr(15, 50, "X:"+str(x)+" ")
        screen.addstr(16, 50, "Y:"+str(y)+" ")
        screen.addstr(17, 50, "Point:"+str(point)+" ")
                
        screen.addstr(y, x, main)

        screen.refresh()
        keycode = screen.getch()
        if keycode == ord("q"):
            break
        if keycode == ord(" "):
            main = "O"
        if keycode == curses.KEY_LEFT:
            if x == 1:
                pass
            else:
                x = x - 1
                f = x + 1
            screen.addstr(y, f,  " ")
        if keycode == curses.KEY_RIGHT:
            if x == 24:
                pass
            else:
                x = x + 1
                a = x - 1
            screen.addstr(y, a,  " ")
        if keycode == curses.KEY_UP:
            if y == 1:
                pass
            else:
                y = y - 1
                b = y + 1
            screen.addstr(b, x,  " ")
        if keycode == curses.KEY_DOWN:
            if y == 24:
                pass
            else:
                y = y + 1
                c = y - 1
            screen.addstr(c, x,  " ")
        if chr(screen.inch(y,x)) == "$":
            point = point + 1
    if point == 5:
        screen.clear()
        screen.addstr(15, 50, "YOU BEAT THE GAME!!!!")
        screen.getch()




if __name__ == "__main__":
    curses.wrapper(main)
