import pygame
from pygame.locals import *
pygame.init()

BLACK = 255,255,0
LILA = 255,0,255
movingRight = True
screen=pygame.display.set_mode((1600,900),FULLSCREEN|HWSURFACE|DOUBLEBUF)
#pygame.display.set_caption("Game")

rect = pygame.Rect((0,425,100,50))



def drawRect():
  global movingRight
  pygame.draw.rect(screen,LILA,rect,0)
  if movingRight:
    rect.left+=15
    if rect.right > 1600:
      movingRight = False
  else:
    rect.left-=15
    if rect.left < 0:
      movingRight = True

clock=pygame.time.Clock()
running=True

while running:
  for e in pygame.event.get():
    if e.type == QUIT:
      running=False
    if e.type == KEYDOWN and e.key == K_ESCAPE:
      running=False
  screen.fill(BLACK)
  drawRect()
  pygame.display.flip()
  clock.tick(50)
  
pygame.quit()
