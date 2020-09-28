import pygame as pg

pg.init()

from consts import *
import menu
import reactions

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE_TEXT)

menu = menu.Menu(win)
reactions = reactions.Reactions(win)

clock = pg.time.Clock()

is_running = True

if __name__ == '__main__':
    selection = menu.start()

    if selection == 'Reactions':
        reactions.start()

    pg.quit()
