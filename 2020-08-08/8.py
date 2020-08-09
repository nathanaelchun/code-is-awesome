import curses
from time import sleep

def main(screen):
    x = 1
    y = 10
    main = "d"
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
            x = x - 1
            f = x + 1
            screen.addstr(y, f,  " ", curses.COLOR_RED)
        if keycode == curses.KEY_RIGHT:
            x = x + 1
            a = x - 1
            screen.addstr(y, a,  " ", curses.COLOR_RED)
        if keycode == curses.KEY_UP:
            y = y - 1
            b = y + 1
            screen.addstr(b, x,  " ", curses.COLOR_RED)
        if keycode == curses.KEY_DOWN:
            y = y + 1
            c = y - 1
            screen.addstr(c, x,  " ", curses.COLOR_RED)


if __name__ == "__main__":
    curses.wrapper(main)