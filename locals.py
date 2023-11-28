import pygame
from pygame.locals import *

import math

pygame.init()

# LOCALS --------------------------------------------------------- #
# Colours
CELL_BG = '#003333'
CELL_4C = '#005555'
CELL_OL = '#ffffff'
BUTTON_BG = '#008888'
PINK = '#ff00ff'
RED = '#ff0000'
DARK_PINK = '#aa00aa'

# Scale 
SCALE = 1
CELL_HEIGHT = 22
CELL_WIDTH = 148

HAR_INC = math.pow(2, 1/12)

# Timing
BPM = 120 # beats/minute
FRAME_RATE = 60 # frames/second
'''
Ticks per Cell:
    60 * FRAME_RATE frames/minute
    BPM / (60 * FRAME_RATE) beats/frame
    (60 * FRAME_RATE) / BPM frames/beat
'''
TPC = int((60 * FRAME_RATE) / (4 * BPM)) # ticks per cell
BAR_LEN = 16

# FONTS ---------------------------------------------------------- #
cell_font = pygame.font.SysFont('Courier New', 16*SCALE)
title_font = pygame.font.SysFont('Arial', 32*SCALE, True, True)
option_font = pygame.font.SysFont('Arial', 20*SCALE)