import curses
from time import sleep


def main(screen):
    x = 2
    y = 10
    wall_x = 0
    wall_x2 = 25
    wall_y2 = 0
    wall_y3 = 25
    main = "d"
    for wall_y in range(0, 26):
        screen.addstr(wall_y, wall_x, "#", curses.COLOR_RED)
        screen.addstr(wall_y, wall_x2, "#", curses.COLOR_RED)
    for wall_x3 in range(0, 26):
        screen.addstr(wall_y2, wall_x3, "#", curses.COLOR_RED)
        screen.addstr(wall_y3, wall_x3, "#", curses.COLOR_RED)
    while True:
        curses.curs_set(0)
        screen.addstr(y, x, main, curses.COLOR_RED)
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
            screen.addstr(y, f,  " ", curses.COLOR_RED)
        if keycode == curses.KEY_RIGHT:
            if x == 24:
                pass
            else:
                x = x + 1
                a = x - 1
            screen.addstr(y, a,  " ", curses.COLOR_RED)
        if keycode == curses.KEY_UP:
            if y == 1:
                pass
            else:
                y = y - 1
                b = y + 1
            screen.addstr(b, x,  " ", curses.COLOR_RED)
        if keycode == curses.KEY_DOWN:
            if y == 24:
                pass
            else:
                y = y + 1
                c = y - 1
            screen.addstr(c, x,  " ", curses.COLOR_RED)


if __name__ == "__main__":
    curses.wrapper(main)
