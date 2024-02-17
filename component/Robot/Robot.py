import pygame

from images.image_loader.images import Images
from consts.game import TILE_SIZE, ROBOT_SIZE, TILE_COLUMN_COUNT
from utils.coordinates import get_coordinates_from_grid

class Robot:
    number_of_frames = 17
    standing_animation_speed = 3
    walking_animation_speed = 1
    animation_speed = standing_animation_speed
    animation_timer = 1
    walking_speed = 2

    def __init__(self, screen, tile = (0, 1), size = (ROBOT_SIZE, ROBOT_SIZE), on_death = None, health = 10):
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

        self.on_death = on_death
        self.health = health
        self.is_alive = True

    @staticmethod
    def get_coordinates(tile):
        return get_coordinates_from_grid(tile, TILE_SIZE, (0, 15))

    @property
    def coordinates(self):
        return  Robot.get_coordinates(self.tile)

    def __do_nothing_if_dead(function):
        def wrapper(self, *args, **kwargs):
            if self.is_alive:
                return function(self, *args, **kwargs)
        return wrapper

    @__do_nothing_if_dead
    def __animate(self):
        self.animation_timer += 1
        if self.animation_timer > self.animation_speed:
            self.current_frame =  (self.current_frame + 1) % self.number_of_frames
            self.animation_timer = 0

    @__do_nothing_if_dead
    def __move(self):
        self.animation_speed = self.walking_animation_speed
        self.rect.x += self.walking_speed

    @__do_nothing_if_dead
    def move_tile(self):
        self.future_position = self.rect.x + TILE_SIZE
        self.tile = (self.tile[0] + 1, self.tile[1])

    def draw(self):
        self.__animate()
        self.screen.blit(self.frames[self.current_frame], self.rect)

        #draw hitbox
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)

        if self.rect.x >= self.future_position:
            self.animation_speed = self.standing_animation_speed
            self.future_position = self.rect.x
            self.rect.topleft = self.coordinates
        else:
            self.__move()

        self.__check_if_in_screen()

    @__do_nothing_if_dead
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.__died()

    @__do_nothing_if_dead
    def __died(self):
        self.is_alive = False
        self.frames[13] = pygame.transform.flip(Images.Robot[13] , True, True)
        self.rect.y += self.rect.height - 10
        self.current_frame = 13
        if self.on_death:
            self.on_death()
    
    @__do_nothing_if_dead
    def __check_if_in_screen(self):
        if self.tile[0] > TILE_COLUMN_COUNT - 1:
            self.__died()