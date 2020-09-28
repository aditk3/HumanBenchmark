from collections import namedtuple
import pygame as pg

# Setup
WIDTH, HEIGHT = 1920, 1080
MENU_FPS = 15

WAIT_TIME = 2500

# Color
BLACK = (0, 0, 0)
BLUE = (43, 135, 209)
LIGHT_BLUE = (193, 220, 242)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Fonts
BUTTON_FONT = pg.font.SysFont('arial', 40)
TITLE_FONT = pg.font.SysFont('arial', 140)
SUBTITLE_FONT = pg.font.SysFont('arial', 45)

# Text
TITLE_TEXT = 'Human Benchmark'
GAME_NAMES = ['Aim', 'Chimp Test', 'Hearing', 'Num. Mem.', 'Reactions', 'Typing', 'Verbal Mem.', 'Visual Mem.']
