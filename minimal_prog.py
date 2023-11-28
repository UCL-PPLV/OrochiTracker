import pygame
from pygame.locals import *
import sys

# Initialize Pygame
pygame.init()

# Define the set of common colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(50, 50, 255)
RED = pygame.Color(255, 50, 50)

# Set the FPS
FPS = pygame.time.Clock()
FPS.tick(30)

# Creates the display surface
DISPLAYSURF = pygame.display.set_mode((500,400))
DISPLAYSURF.fill(WHITE)


while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

    pygame.display.update()

