import pygame
import pygame_gui
import sys

from scenes.Main import Main

pygame.init()

SCREEN_DIMENSIONS = (1200, 896)

if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    manager = pygame_gui.UIManager(SCREEN_DIMENSIONS)
    pygame.display.set_caption('MetaBot')
    Main(screen, manager)()
    pygame.quit()
    sys.exit(0)