import pygame

from component.Monsters.MonsterBase import MonsterBase
from images.image_loader.images import Images
from consts.game import TILE_SIZE
from utils.coordinates import get_coordinates_from_grid


class Spikes(MonsterBase):
    damage = 1
    alive_timer = 20

    def __init__(self, screen, tile, player):
        self.screen = screen
        self.tile = tile
        self.original_image = pygame.transform.scale(
            Images.Spikes, (TILE_SIZE, TILE_SIZE))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.topleft = self.coordinates
        self.hitbox = self.rect.inflate(-TILE_SIZE // 1.2, -40)
        super().__init__(self.damage, player, self.hitbox)

    @property
    def coordinates(self):
        return get_coordinates_from_grid(self.tile, TILE_SIZE)

    def update(self):
        if self.has_taken_damage:
            self.alive_timer -= 1

        if self.alive_timer > 0:
            self.screen.blit(self.image, self.rect)
            super().update()
