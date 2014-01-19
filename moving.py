import pygame
from pygame.locals import *
from random import randint
pygame.init()
pygame.mouse.set_visible(False)

BGCOLOR = (150,255,160)
COLOR = (120,182,80)
HSPEED = 20
VSPEED = 15
FONTSIZE = 100

screen = pygame.display.set_mode((1600,900),FULLSCREEN)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, FONTSIZE)
isRunning = True
move = [False, False]
rect = pygame.Rect((700,785,200,30))
ball = pygame.Rect((785,0,30,30))
ballV = VSPEED
points = 0

def getInput():
    isRunning = True
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                isRunning = False
            elif event.key == K_LEFT:
                move[0] = True
            elif event.key == K_RIGHT:
                move[1] = True
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move[0] = False
            if event.key == K_RIGHT:
                move[1] = False
    return isRunning

def update():
    global ballV,points
    if move[0] and not rect.left <=0:
        rect.move_ip(-HSPEED,0)
    if move[1] and not rect.right >= 1600:
        rect.move_ip(HSPEED,0)
    
    ball.move_ip(0,ballV)
    if ball.top >= 900:
        #ballV = -VSPEED
        newBall()
    if ball.bottom < 0:
        newBall()
    if ball.colliderect(rect) and ballV > 0 and not ball.top > rect.top:
        ballV=-VSPEED
        points += 1

def draw():
    screen.fill(BGCOLOR)
    screen.fill(COLOR,rect)
    screen.fill(COLOR,ball)
    text = font.render("%02d"%points,True,COLOR,BGCOLOR)
    fps = font.render("%.2f" % clock.get_fps(),True,COLOR,BGCOLOR)
    screen.blit(text,(50,50))
    screen.blit(fps, (1400,50))
    pygame.display.flip()
    
def newBall():
    global ballV
    ball.topleft = (randint(0,1580),0)
    ballV=VSPEED
    
while isRunning:
    isRunning = getInput()
    update()
    draw()
    clock.tick(30)

pygame.quit()