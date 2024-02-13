import pygame
import sys
from component.Gear.GearButton import GearButton
from component.Gear.GearMouse import GearMouse

pygame.init()

SCREEN_DIMENSIONS = (1200, 896)
BG = (0, 0, 0)
FPS = 60

class Main:
    def __init__(self, screen):
        self.mouse = GearMouse.get_instance(screen)

        self.gear = GearButton(screen, 100, (100, 100), lambda: print("Clicked"))

    def __call__(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            screen.fill(BG)
            self.gear.draw()

            if any(event.type == pygame.QUIT
                for event in pygame.event.get()):
                break

            self.mouse.draw()
            pygame.display.update()


if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption('MetaBot')
    Main(screen)()
    pygame.quit()
    sys.exit(0)