import curses
from time import sleep

def main(screen):
    for x in range(1,50):
        screen.addstr(10, x, "-->", curses.COLOR_RED)
        screen.refresh()
        sleep(0.05)
        screen.addstr(10, x,  "   ", curses.COLOR_RED)

    screen.addstr(15, 9, "Polar Bear", curses.A_BLINK)

    screen.getch()

if __name__ == "__main__":
    curses.wrapper(main)