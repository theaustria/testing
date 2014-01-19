import pygame
pygame.init()

windowSurface = pygame.display.set_mode((500, 400))         # erzeuge Fenster der Größe 500x400
pygame.display.set_caption('Hello world!')                  # ändere Titel in "Hello World"
basicFont = pygame.font.SysFont(None, 48)                   # erzeugt Font-Objekt mit dem Standard-Font und der Größe 48
text = basicFont.render('Hello world!', True, WHITE, BLUE)  # erzeugt Surface mit gerendertem Text, True für Antialiasing, Farben
textRect = text.get_rect()                                  # Rechteck um Text
textRect.centerx = windowSurface.get_rect().centerx         # verschiebe Text in Mitte von Surface
textRect.centery = windowSurface.get_rect().centery         #
windowSurface.fill(WHITE)                                   # Surface mit einer Farbe füllen

pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))  # polygon(Surface, fillColor, Coords)
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)                                       # line(Surface, color, start, end, width)
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)                                           # circle(Surface, color, center, radius, width)
pygame.draw.ellipse(windowSurface, BLUE, (100,200,50,150),1)                                        # ellipse(Surface, color,(left,top,width,height), linewidth)
pygame.draw.rect(windowSurface, RED, (100,100,50,100),1)                                            # rect(Surface,color,coords,width)

pixArray = pygame.PixelArray(windowSurface)                 # erzeugt PixelArray
windowSurface.blit(text, textRect)                          # Surface.blit(source,pos) kopiert source-Surface an Pos
pygame.display.update()                                     # Bildschirm aktualisieren

for event in pygame.event.get():                            #
   if event.type == QUIT:                                   # wenn beenden-event, dann beenden