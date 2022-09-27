import math
import pygame
from pygame import gfxdraw
import colors

def init():
    print('Starting...')

def loop():
    height = pygame.display.get_surface().get_height()
    width = pygame.display.get_surface().get_width()

    screen.fill(colors.BACKGROUND)
    drawSineCurve(.20 * height, colors.CURVES[0], height, width)
    drawSineCurve(.50 * height, colors.CURVES[1], height, width)
    drawSineCurve(.80 * height, colors.CURVES[2], height, width)

def drawSineCurve(y_level, color, height, width):
    positions = [(width, height), (0, height)]
    for x in range(0, math.ceil(width/16+1)):
        pos = (x*16, math.sin((x+frame)/16+y_level)*16 + y_level)
        positions.append(pos)
    gfxdraw.aapolygon(screen, positions, color)
    gfxdraw.filled_polygon(screen, positions, color)

def onEvent(event):
    if event.type == pygame.QUIT:
        pygame.quit()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Sinus Wallpaper")
    clock = pygame.time.Clock()
    
    init()

    frame = 0

    while True:
        frame += .1
        for event in pygame.event.get():
            onEvent(event)

        loop()
        pygame.display.flip()
        clock.tick(60)