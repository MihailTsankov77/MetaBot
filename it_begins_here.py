import pygame
import sys
from component.Gear.GearButton import GearButton

pygame.init()

SCREEN_DIMENSIONS = (1200, 896)
BG = (0, 0, 0)
FPS = 60


def main(screen):
    clock = pygame.time.Clock()


    gear = GearButton(screen, (100, 100), (100, 100), lambda: print("Clicked"))

    while True:
        clock.tick(FPS)
        screen.fill(BG)
        gear.draw()

        if any(event.type == pygame.QUIT
            for event in pygame.event.get()):
            break
        pygame.display.update()


if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption('MetaBot')
    main(screen)
    pygame.quit()
    sys.exit(0)