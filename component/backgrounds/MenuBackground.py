import pygame

from images.image_loader.images import Images
from consts.game import  SCREEN_DIMENSIONS

class MenuBackground:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(Images.MenuBackground, SCREEN_DIMENSIONS)
        self.rect = self.image.get_rect()

    def update(self):
        self.screen.blit(self.image, self.rect)