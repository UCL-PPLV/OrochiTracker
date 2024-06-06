import os
import sys
import pygame

from pygame.locals import *
from classes import *
from locals import *
from functions import *
from fonts import *

# Start Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Orochi Tracker')
pygame.display.set_icon(pygame.image.load('logo.png'))

# Create clock object
clock = pygame.time.Clock()

# Print Title
title_text, version_text = make_title(screen)

# Editables
editables = [
    'note',
    'instrument',
    'fx id',
    'fx amt'
]
currently_editing = 1

# Initialize Cells
cell_array = [
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
    [Cell(i, CELL_WIDTH, CELL_HEIGHT, CELL_BG) for i in range(BAR_LEN)],
]

# Active cells 
active = [0 for col in cell_array]  # Playing
selected = [0, 0]                   # Editing

# Instruments
instrument_files = os.listdir('samples')
instruments = [
    pygame.mixer.Sound(os.path.join('samples', f)) for f in instrument_files
]

# Initialize playing and countdown
playing = [False for col in cell_array]
countdown = TPC

# THE LOOP #
while True :

    # Loop through columns
    for i in range(len(cell_array)) :

        # Loop through cells
        for j in range(len(cell_array[i])) :
            # Set current cell
            cell = cell_array[i][j]
            # Determine if active cell is current cell
            is_active = (active[i] == j)
            is_selected = (selected == [i,j])

            # Visual indicator of active cell
            if is_selected :
                cell.surf.fill(RED)
            elif is_active :
                cell.surf.fill(PINK)
            elif j % 4 == 0 :
                cell.surf.fill(CELL_4C)
            else : 
                cell.surf.fill(CELL_BG)

            # Fill cells with info text
            cell_text = cell_font.render(cell.get_info(), True, '#ffffff', '#000000')
            cell.surf.blit(cell_text, (1, 1))

            # Print cells
            screen.blit(cell.surf, ((CELL_WIDTH + 2) * SCALE * i, 400*SCALE + CELL_HEIGHT * SCALE * j + 1))

    # Update currently editing
    pygame.draw.rect(screen, BUTTON_BG, pygame.Rect(658, 8, 300, 35))
    screen.blit(
        option_font.render('Editing', False, '#ffffff'),
        (665, 12)
    )
    screen.blit(
        cell_font.render(editables[currently_editing], False, '#ffffff'), (740, 15)
    )

    # Update File List
    pygame.draw.rect(screen, BUTTON_BG, pygame.Rect(253, 8, 400, 35 + 18*len(instrument_files)))
    screen.blit(
        option_font.render('Instruments', False, '#ffffff'),
        (260, 12)
    )
    for i in range(len(instrument_files)) :
        screen.blit(
            cell_font.render(f'{i:3} | {instrument_files[i]}', False, '#ffffff'),
            (275, 35 + 18*i)
        )

    # Countdown events: 
    # - if the countdown is zero, advance all the columns and reset the timer
    # - otherwise, countdown
    if countdown <= 0 :
        for i in range(len(cell_array)) :
            if playing[i] :
                try :
                    if playing[i] :
                        cell = cell_array[i][active[i]]

                        # PLAY THE SAMPLE
                        play_cell(
                            instruments[cell.inst],
                            cell.note,
                            cell.fx1_num,
                            cell.fx1_amt
                        )
                except :
                    pass
                if cell.fx1_num == 1 :
                            active[i] = cell.fx1_amt % len(cell_array[i])
                else :
                    active[i] = (active[i] + 1) % len(cell_array[i])
                
        countdown = TPC
    else :
        if True in playing :
            countdown -= 1
        
    # Event Loop
    for event in pygame.event.get() :
        if event.type == KEYDOWN :
            # Reset column positions
            if event.key == K_RETURN :
                for i in range(len(active)) :
                    active[i] = 0

            # Move the selected cell around, allow for editing
            if event.key == K_UP :
                # Shift means edit mode
                if pygame.key.get_pressed()[K_LSHIFT] :
                    # Grab the cell you're editing
                    cell = cell_array[selected[0]][selected[1]]

                    # Check what is being edited
                    if currently_editing == 1 :
                        # Edit the instrument
                        if cell.inst != None and cell.inst < 99 :
                            cell.inst = cell.inst + 1
                        elif cell.inst == None :
                            cell.inst = 0
                        else :
                            cell.inst = None
                    elif currently_editing == 0 :
                        # Edit the instrument
                        cell.note = (cell.note + 1)%158
                    elif currently_editing == 2 :
                        cell.fx1_num = (cell.fx1_num + 1) % 10
                    elif currently_editing == 3 :
                        cell.fx1_amt = (cell.fx1_amt + 1) % 100
                else :
                    selected[1] = (selected[1] - 1) % len(cell_array[selected[0]])

            if event.key == K_DOWN :
                # Shift means edit mode
                if pygame.key.get_pressed()[K_LSHIFT] :
                    # Grab the cell you're editing
                    cell = cell_array[selected[0]][selected[1]]

                    # Check what is being edited
                    if editables[currently_editing] == 'instrument' :
                        # Edit the instrument
                        if cell.inst != None and cell.inst > 0 :
                            cell.inst = cell.inst - 1
                        else :
                            cell.inst = None
                    elif editables[currently_editing] == 'note' :
                        # Edit the instrument
                        cell.note = (cell.note - 1)%158
                    elif editables[currently_editing] == 'fx id' :
                        cell.fx1_num = (cell.fx1_num - 1) % 10
                    elif editables[currently_editing] == 'fx amt' :
                        cell.fx1_amt = (cell.fx1_amt - 1) % 100
                else :
                    selected[1] = (selected[1] + 1) % len(cell_array[selected[0]])
            
            if event.key == K_RIGHT :
                if pygame.key.get_pressed()[K_LSHIFT] :
                    currently_editing = (currently_editing + 1) % len(editables)
                else :
                    selected[0] = (selected[0] + 1) % len(cell_array)

            if event.key == K_LEFT :
                if pygame.key.get_pressed()[K_LSHIFT] :
                    currently_editing = (currently_editing - 1) % len(editables)
                else :
                    selected[0] = (selected[0] - 1) % len(cell_array)

            # Play all columns
            if event.key == K_SPACE :
                if True in playing :
                    for i in range(len(playing)) :
                        playing[i] = False
                else :
                    countdown = TPC
                    for i in range(len(playing)) :
                        playing[i] = True

        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(FRAME_RATE)
    