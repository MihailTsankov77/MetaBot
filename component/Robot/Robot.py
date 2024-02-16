import pygame

from images.image_loader.images import Images
from consts.game import TILE_SIZE, ROBOT_SIZE
from utils.coordinates import get_coordinates_from_grid

class Robot:
    number_of_frames = 17
    standing_animation_speed = 3
    walking_animation_speed = 1
    animation_speed = standing_animation_speed
    animation_timer = 1


    walking_speed = 1

    def __init__(self, screen, tile = (0, 1), size = (ROBOT_SIZE, ROBOT_SIZE)):
        self.screen = screen
        transformed_frames = []
        for i in range(self.number_of_frames):
            transformed_frames.append(pygame.transform.scale(Images.Robot[i], size))
        self.frames =  transformed_frames
        self.rect = self.frames[0].get_rect()
        
        self.tile = tile

        self.rect.topleft = self.coordinates

        self.current_frame = 0
        self.future_position = self.rect.x

    @staticmethod
    def get_coordinates(tile):
        return get_coordinates_from_grid(tile, TILE_SIZE, (0, 15))

    @property
    def coordinates(self):
        return  Robot.get_coordinates(self.tile)

    def animate(self):
        self.animation_timer += 1
        if self.animation_timer > self.animation_speed:
            self.current_frame =  (self.current_frame + 1) % self.number_of_frames
            self.animation_timer = 0

    def move(self):
        self.animation_speed = self.walking_animation_speed
        self.rect.x += self.walking_speed

    def move_tile(self):
        self.future_position = self.rect.x + TILE_SIZE
        self.tile = (self.tile[0] + 1, self.tile[1])

    def draw(self):
        self.animate()
        self.screen.blit(self.frames[self.current_frame], self.rect)

        if self.rect.x >= self.future_position:
            self.animation_speed = self.standing_animation_speed
            self.future_position = self.rect.x
            self.rect.topleft = self.coordinates
        else:
            self.move()
