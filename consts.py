from collections import namedtuple
import pygame as pg

# Setup
WIDTH, HEIGHT = 1080, 720
MENU_FPS = 15

# Color
BLACK = (0, 0, 0)
BLUE = (43, 135, 209)
LIGHT_BLUE = (193, 220, 242)
WHITE = (255, 255, 255)

# Fonts
BUTTON_FONT = pg.font.SysFont('arial', 40)
TITLE_FONT = pg.font.SysFont('arial', 120)
SUBTITLE_FONT = pg.font.SysFont('arial', 40)

# Text
TITLE_TEXT = 'Human Benchmark'
GAME_NAMES = ['Aim', 'Chimp Test', 'Hearing', 'Num. Mem.', 'Reactions', 'Typing', 'Verbal Mem.', 'Visual Mem.']

