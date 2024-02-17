import pygame
import pygame_gui
import sys
# from  text_parsers.from_file_to_text.file_parser import parse_file

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

# with open('text_parsers/from_file_to_text/test/TestObject.py', 'r') as file:
#     print(parse_file(file, ['x']))

