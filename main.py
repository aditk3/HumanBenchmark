import pygame as pg
pg.init()

from consts import *
import menu

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE_TEXT)

menu = menu.Menu(win)

clock = pg.time.Clock()

is_running = True

if __name__ == '__main__':
    menu.menu()

    pg.quit()
