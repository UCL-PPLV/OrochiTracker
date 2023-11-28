import pygame
from pygame.locals import *
from locals import *

import numpy
#from scikits.samplerate import resample
import pygame.sndarray as snd

# Functions -------------------------- #
def make_title(screen) :
    title_text = title_font.render('Orochi Tracker', False, '#ffffff')
    version_text = cell_font.render('ver 0.1', False, '#ffffff')
    title_box = pygame.draw.rect(screen, BUTTON_BG, pygame.Rect(8, 8, 240, 50) )
    screen.blit(title_text, (10, 10))
    screen.blit(version_text, (20, 40))
    return [title_text, version_text]

def play_cell(inst_file, note, fx1_num, fx_amt) :
    ary = snd.array(inst_file)
    #mod_ary = resample(ary).astype(ary.dtype)
    #mod_ary.play()
    inst_file.play()