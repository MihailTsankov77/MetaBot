import pygame
import pygame_gui
import sys

from scenes.Main import Main
from consts.game import SCREEN_DIMENSIONS

pygame.init()


if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    manager = pygame_gui.UIManager(SCREEN_DIMENSIONS)
    pygame.display.set_caption('MetaBot')
    Main(screen, manager)()
    pygame.quit()
    sys.exit(0)


# TODO fix imports

