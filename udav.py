import pygame
import sys
import time
from pygame.locals import *

x = 30
y = 20
pole = [[0] * y for i in range(x)]
headX = 10
headY = 10
pole[headX][headY]=2

pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
width=x*32
height=y*32
mainSurface=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Keyb moves')
spriteBlack=pygame.image.load('images//black.jpg')
spriteGreen=pygame.image.load('images//green.jpg')
spriteRed=pygame.image.load('images//red.jpg')

direction=False

for m in range(x):
    pole[m][0] = 1
    pole[m][19] = 1
for n in range(y):
    pole[0][n] = 1
    pole[29][n] = 1    

def update_pole(mainSurface):
    for m in range(x):
        for n in range(y):
            if pole[m][n]==0:
                mainSurface.blit(spriteBlack,(m*32,n*32))
            if pole[m][n]==1:
                mainSurface.blit(spriteGreen,(m*32,n*32))
            if pole[m][n]==2:
                mainSurface.blit(spriteRed,(m*32,n*32))
    return mainSurface

def move(direction,headX,headY,pole):
    if direction:
        pole[headX][headY] = 0
        if direction == K_UP:
            if pole[headX][headY-1]==0:
                headY -= 1
        elif direction == K_DOWN:
            if pole[headX][headY+1]==0:
                headY += 1
        if direction == K_LEFT:
            if pole[headX-1][headY]==0:
                headX -= 1
        elif direction == K_RIGHT:
            if pole[headX+1][headY]==0:
                headX += 1
        pole[headX][headY] = 2
    return headX,headY,pole

while True:
    fpsClock.tick(FPS) # define frame rate
    mainSurface = update_pole(mainSurface)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN: direction = event.key # Other key pressed
        if event.type == KEYUP:  direction = False # Key released

    headX,headY,pole = move(direction,headX,headY,pole)

    pygame.display.update()

