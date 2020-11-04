import pygame as pg
from consts import *


class ChimpTest():

    def __init__(self, win):
        self.win = win

        self.circle_count = 4
        self.is_hidden = False
        self.is_running = False


    def start(self):
        round_started = False

        self.is_running = True
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                    pg.quit()
                    quit()

            if not round_started:
                self.draw_start_screen()

            pg.display.update()


    def draw_start_screen(self):
        self.win.fill(BLUE)

        title_text = TITLE_FONT.render('Are You Smarter Than A Chimpanzee', 1, WHITE)
        self.win.blit(title_text, ((WIDTH / 2 - title_text.get_width() / 2), ((40 * HEIGHT) // 720) + 50))

        subtitle_text = SUBTITLE_FONT.render('Click the squares in order according to their numbers.', 1,
                                             LIGHT_BLUE)
        self.win.blit(subtitle_text, (
        (WIDTH / 2 - subtitle_text.get_width() / 2), HEIGHT - ((160 * HEIGHT) // 720) - subtitle_text.get_height()))

        subtitle_text = SUBTITLE_FONT.render('The test will get progressively harder.', 1,
                                             LIGHT_BLUE)
        self.win.blit(subtitle_text, ((WIDTH / 2 - subtitle_text.get_width() / 2), HEIGHT - ((160 * HEIGHT) // 720)))
