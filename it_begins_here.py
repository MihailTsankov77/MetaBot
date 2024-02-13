import pygame
import sys

pygame.init()

SCREEN_DIMENSIONS = (1200, 896)
FPS = 60


def main(screen):
    clock = pygame.time.Clock()
    # sprite_sheet = SpriteSheet()
    # world = GameWorld(screen, sprite_sheet)
    # player = Player(200, 600, screen, sprite_sheet, world)
    while True:
        clock.tick(FPS)
        world.render_world()
        player.update()
        if any(event.type == pygame.QUIT
            for event in pygame.event.get()):
            break
        pygame.display.update()


if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption('Super Jorgtor')
    main(screen)
    pygame.quit()
    sys.exit(0)