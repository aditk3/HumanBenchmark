import pygame as pg
from consts import *
import math


class Menu:
    # Button vars
    RADIUS = (100 * HEIGHT) // 720
    GAP = (65 * HEIGHT) // 720


    def __init__(self, win):
        self.win = win
        self.is_running = True
        self.clock = pg.time.Clock()

        self.game_names = []
        self.start_x = ((round(((WIDTH - (self.RADIUS * 2 + self.GAP) * 4) / 2)) * HEIGHT) // 720) - (60 * HEIGHT) // 720
        self.start_y = (370 * HEIGHT) // 720 - 50

        # Set up button locations and text
        for i in range(8):
            x = self.start_x + self.GAP * 2 + (self.RADIUS * 2 + self.GAP) * (i % 4)
            y = self.start_y + ((i // 4) * (self.GAP - 40 * (i // 4) + self.RADIUS * 2))
            self.game_names.append((x, y, GAME_NAMES[i]))


    def draw_titles(self):
        title_text = TITLE_FONT.render(TITLE_TEXT, 1, WHITE)
        self.win.blit(title_text, ((WIDTH / 2 - title_text.get_width() / 2), (40 * HEIGHT) // 720))

        subtitle_text = SUBTITLE_FONT.render('Measure your abilities with brain games and cognitive tests', 1,
                                             LIGHT_BLUE)
        self.win.blit(subtitle_text, ((WIDTH / 2 - subtitle_text.get_width() / 2), ((160 * HEIGHT) // 720) - 30))


    def draw(self):
        self.win.fill(BLUE)
        self.draw_titles()

        # Draw buttons
        for game_name in self.game_names:
            color = LIGHT_BLUE
            x, y, name = game_name

            # Change color is mouse is hovering over the button
            m_x, m_y = pg.mouse.get_pos()
            dist = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dist < self.RADIUS:
                color = WHITE

            pg.draw.circle(self.win, color, (x, y), self.RADIUS, 4)

            text = BUTTON_FONT.render(name, 1, color)
            self.win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))


    def start(self):
        self.is_running = True

        while self.is_running:
            self.clock.tick(MENU_FPS)
            to_return = None

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                    break

                # Returns game user clicked on
                if event.type == pg.MOUSEBUTTONDOWN:
                    m_x, m_y = pg.mouse.get_pos()
                    for game_name in self.game_names:
                        x, y, name = game_name
                        dist = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dist < self.RADIUS:
                            to_return = name

            self.draw()
            pg.display.update()

            if to_return:
                self.is_running = False
                return to_return
