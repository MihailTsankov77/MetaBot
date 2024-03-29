import pygame
from images.image_loader.images import Images


class Gear:
    def __init__(self, screen, size, position):
        self.screen = screen
        self.original_image = pygame.transform.scale(Images.Gear, (size, size))
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.rect.center = position
        self.angle = 0

    def rotate(self, speed=1):
        self.angle += speed

        rotated_image = pygame.transform.rotate(
            self.original_image, self.angle % 360)
        new_rect = rotated_image.get_rect(center=self.rect.center)

        self.image = rotated_image
        self.rect = new_rect

    def set_position(self, position):
        self.rect.center = position

    def update(self):
        self.screen.blit(self.image, self.rect)
