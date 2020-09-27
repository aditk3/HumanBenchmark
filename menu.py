import pygame as pg
from consts import *
import math


class Menu:
    # Button vars
    RADIUS = 100
    GAP = 65
    GAME_NAMES = ['Aim', 'Ape Test', 'Hearing', 'Num. Mem.', 'Reactions', 'Typing', 'Verbal Mem.', 'Visual Mem.']

    # Fonts
    BUTTON_FONT = pg.font.SysFont('arial', 40)


    def __init__(self, win):
        self.win = win
        self.is_running = True
        self.clock = pg.time.Clock()

        self.game_names = []
        self.start_x = round((WIDTH - (self.RADIUS * 2 + self.GAP) * 4) / 2)
        self.start_y = 370

        print(self.start_x)

        # Set up button locations and text
        for i in range(8):
            x = self.start_x + self.GAP * 2 + (self.RADIUS * 2 + self.GAP) * (i % 4)
            y = self.start_y + ((i // 4) * (self.GAP - 40 * (i // 4) + self.RADIUS * 2))
            # self.game_names.append((x, y))
            self.game_names.append((x, y, self.GAME_NAMES[i]))


    def draw(self):
        self.win.fill(BLUE)

        # Draw buttons
        for game_name in self.game_names:
            x, y, name = game_name
            pg.draw.circle(self.win, LIGHT_BLUE, (x, y), self.RADIUS, 4)

            # Change text color is mouse is hovering over the button
            text_color = LIGHT_BLUE
            m_x, m_y = pg.mouse.get_pos()
            dist = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dist < self.RADIUS:
                text_color = WHITE

            text = self.BUTTON_FONT.render(name, 1, text_color)
            self.win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))


    def menu(self):
        while self.is_running:
            self.clock.tick(MENU_FPS)

            to_return = None

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False

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