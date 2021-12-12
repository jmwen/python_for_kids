import pygame, sys
pygame.init()
dots = [[320, 240], [320, 300], [340, 340], [320, 300],
        [300, 340], [320, 300], [320, 240], [340, 280],
        [320, 240], [300, 280]]
doti = [[285, 180], [355, 180], [345, 180], [345, 110],
        [295, 110], [295, 180]]
dotsi = [[313, 225], [327, 225]]
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [0,0,0], [320, 210], 30, 2)
pygame.draw.lines(screen, [0,0,0],True, dots, 2)
pygame.draw.lines(screen, [0,0,0],True, doti, 2)
pygame.draw.lines(screen, [0,0,0],True, dotsi, 2)
pygame.draw.circle(screen, [0,0,0], [310, 205], 2, 2)
pygame.draw.circle(screen, [0,0,0], [330, 205], 2, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()