import pygame as pg
from consts import *


class Reactions:
    def __init__(self, win):
        self.win = win
        self.is_running = True
        self.clock = pg.time.Clock()


    def start(self):
        while self.is_running:
            self.draw_start_screen()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                    break

                if event.type == pg.MOUSEBUTTONDOWN:
                    # TODO: Implement reaction time game
                    pass

            pg.display.update()


    def draw_start_screen(self):
        self.win.fill(BLUE)

        title_text = TITLE_FONT.render('Reaction Time', 1, WHITE)
        self.win.blit(title_text, ((WIDTH / 2 - title_text.get_width() / 2), ((40 * HEIGHT) // 720) + 50))

        subtitle_text = SUBTITLE_FONT.render('Click anywhere to begin', 1,
                                             LIGHT_BLUE)
        self.win.blit(subtitle_text, ((WIDTH / 2 - subtitle_text.get_width() / 2), HEIGHT - ((160 * HEIGHT) // 720)))
