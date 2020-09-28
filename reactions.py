import pygame as pg
from consts import *
from random import randint


class Reactions:
    ROUNDS = 5
    MIN_ROUND_TIME = 1.5
    MAX_ROUND_TIME = 5

    RECT_WIDTH, RECT_HEIGHT = 960, 540


    def __init__(self, win):
        self.win = win
        self.is_running = True
        self.clock = pg.time.Clock()
        self.score = 0
        self.green = False


    def start(self):
        finished = False

        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                    break

                if event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(self.ROUNDS):
                        # Checks if close button was pressed during the round
                        if not self.is_running:
                            break

                        self.score += self.run_round()

                    finished = True

            if not finished:
                self.draw_start_screen()

            else:
                final_score = self.score // self.ROUNDS
                self.draw_score(final_score)
                pg.display.update()
                self.is_running = False
                return final_score

            pg.display.update()


    def draw_start_screen(self):
        self.win.fill(BLUE)

        title_text = TITLE_FONT.render('Reaction Time', 1, WHITE)
        self.win.blit(title_text, ((WIDTH / 2 - title_text.get_width() / 2), ((40 * HEIGHT) // 720) + 50))

        subtitle_text = SUBTITLE_FONT.render('Click anywhere to begin', 1,
                                             LIGHT_BLUE)
        self.win.blit(subtitle_text, ((WIDTH / 2 - subtitle_text.get_width() / 2), HEIGHT - ((160 * HEIGHT) // 720)))


    def run_round(self):
        self.green = False
        start_time = pg.time.get_ticks()
        round_time = randint(int(self.MIN_ROUND_TIME * 1000), int(self.MAX_ROUND_TIME * 1000))

        while True:
            for event in pg.event.get():
                self.win.fill(BLUE)

                if event.type == pg.QUIT:
                    self.is_running = False
                    pg.quit()
                    quit()

                # Starts a new round if the user clicked too early
                if event.type == pg.MOUSEBUTTONDOWN and not self.green:
                    self.draw_too_early()
                    pg.display.update()
                    pg.time.delay(3000)
                    return self.run_round()

                if event.type == pg.MOUSEBUTTONDOWN and self.green:
                    time_taken = pg.time.get_ticks() - (start_time + round_time)
                    self.draw_time_taken(str(time_taken) + 'ms')
                    return time_taken

            if pg.time.get_ticks() > start_time + round_time:
                self.green = True

            if self.green:
                pg.draw.rect(self.win, GREEN, (
                    (WIDTH / 2 - self.RECT_WIDTH / 2), HEIGHT / 2 - self.RECT_HEIGHT / 2, self.RECT_WIDTH,
                    self.RECT_HEIGHT))

            else:
                pg.draw.rect(self.win, RED, (
                    (WIDTH / 2 - self.RECT_WIDTH / 2), HEIGHT / 2 - self.RECT_HEIGHT / 2, self.RECT_WIDTH,
                    self.RECT_HEIGHT))
                
                self.draw_subtitle_to_center('Click on green...')

            pg.display.update()


    def draw_too_early(self):
        self.win.fill(RED)

        self.draw_subtitle_to_center('Too Early')


    def draw_subtitle_to_center(self, text):
        text = SUBTITLE_FONT.render(text, 1, WHITE)
        self.win.blit(text, ((WIDTH / 2 - text.get_width() / 2), (HEIGHT / 2 - text.get_height() / 2)))


    def draw_time_taken(self, time):
        self.win.fill(BLUE)
        self.draw_subtitle_to_center(time)
        pg.display.update()
        pg.time.delay(3000)


    def draw_score(self, score):
        self.win.fill(BLUE)
        self.draw_subtitle_to_center('Your average time is ' + str(score) + 'ms')
        pg.display.update()

        pg.time.delay(3000)
