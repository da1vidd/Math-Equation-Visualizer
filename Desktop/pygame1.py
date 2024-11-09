import pygame 
import sys 
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((800,800)) 
DISPLAYSURF.fill(blue)
pygame.display.set_caption("Game") 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()