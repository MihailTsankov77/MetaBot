import pygame

from images.image_loader.images import Images
from consts.game import TILE_SIZE, SCREEN_WIDTH

class Background:
    offset_y = 2 * TILE_SIZE

    def __init__(self, screen):
        self.image = Images.Background
        self.flipped_image = pygame.transform.flip(Images.Background , True, False)
        self.screen = screen
        rect = self.image.get_rect()

        width = self.image.get_width() - SCREEN_WIDTH//2

        self.rect = (-width, -self.offset_y, rect[2], rect[3])

        self.flipped_rect = (self.image.get_width() - width, -self.offset_y, rect[2], rect[3])

    @property
    def height(self):
        return self.image.get_height() - self.offset_y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.flipped_image, self.flipped_rect)