import pygame as pg

pg.init()

from consts import *
import menu
import reactions

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE_TEXT)

scores = {x: 0 for x in GAME_NAMES}

menu = menu.Menu(win)


clock = pg.time.Clock()

is_running = True

if __name__ == '__main__':
    while True:
        selection = menu.start()

        if selection == 'Reactions':
            react = reactions.Reactions(win)
            scores['Reactions'] = react.start()
