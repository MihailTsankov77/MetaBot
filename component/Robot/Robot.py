import pygame
from enum import Enum

from images.image_loader.images import Images
from consts.game import TILE_SIZE, ROBOT_SIZE, TILE_COLUMN_COUNT
from utils.coordinates import get_coordinates_from_grid


class Action(Enum):
    Moving = 1
    TakingDamage = 2,
    Delay = 3


class Robot:
    number_of_frames = 17
    standing_animation_speed = 3
    walking_animation_speed = 1
    animation_speed = standing_animation_speed
    animation_timer = 1
    walking_speed = 2

    def __init__(self, screen,
                 tile,
                 on_death=None,
                 health=10,
                 on_action_finished=None):
        self.screen = screen
        transformed_frames = []
        size = (ROBOT_SIZE, ROBOT_SIZE)
        for i in range(self.number_of_frames):
            transformed_frames.append(
                pygame.transform.scale(Images.Robot[i], size))
        self.frames = transformed_frames
        self.rect = self.frames[0].get_rect()

        self.tile = tile

        self.rect.topleft = self.coordinates

        self.current_frame = 0
        self.future_position = self.rect.x

        self.on_death = on_death
        self.health = health

        self.is_alive = True
        self.is_moving_forward = None

        self.on_action_finished = on_action_finished

        self.in_action = False
        self.current_actions = set()

        self.__delay_timer = 0
        self._is_player_delay = False
        self.future_damage = None

    @staticmethod
    def get_coordinates(tile):
        return get_coordinates_from_grid(tile, TILE_SIZE, (0, 15))

    @property
    def coordinates(self):
        return Robot.get_coordinates(self.tile)

    def __do_nothing_if_dead(function):
        def wrapper(self, *args, **kwargs):
            if self.is_alive:
                return function(self, *args, **kwargs)
        return wrapper

    @__do_nothing_if_dead
    def __animate(self):
        self.animation_timer += 1
        if self.animation_timer > self.animation_speed:
            self.current_frame = (self.current_frame +
                                  1) % self.number_of_frames
            self.animation_timer = 0

    @__do_nothing_if_dead
    def move_tile(self, tiles=1):
        self.current_actions.add(Action.Moving)
        self.is_moving_forward = tiles > 0
        self.future_position = self.rect.x + tiles * TILE_SIZE
        self.tile = (self.tile[0] + tiles, self.tile[1])

    @__do_nothing_if_dead
    def __move(self):
        self.animation_speed = self.walking_animation_speed
        multiplier = 1 if self.is_moving_forward else -1
        self.rect.x += self.walking_speed * multiplier

    @__do_nothing_if_dead
    def __handle_move(self):
        if self.is_moving_forward == None:
            return

        should_stop_moving = ((self.is_moving_forward and self.rect.x >= self.future_position) or
                              (not self.is_moving_forward and self.rect.x <= self.future_position))

        if should_stop_moving:
            self.animation_speed = self.standing_animation_speed
            self.future_position = self.rect.x
            self.rect.topleft = self.coordinates

            self.is_moving_forward = None

            self.current_actions.discard(Action.Moving)
        else:
            self.__move()

    def update(self):
        self.__animate()
        self.screen.blit(self.frames[self.current_frame], self.rect)

        if self.__delay_timer:
            self.__handle_delay()
            return

        self.__execute_take_damage()
        self.__handle_move()
        self.__handle_action_finished()

        self.__check_if_in_screen()
        if self.health <= 0:
            self.__died()

    @__do_nothing_if_dead
    def take_damage(self, damage):
        self.current_actions.add(Action.TakingDamage)
        self.future_damage = damage

    @__do_nothing_if_dead
    def __execute_take_damage(self):
        if not self.future_damage:
            return

        self.health -= self.future_damage
        self.future_damage = None
        if self.health <= 0:
            self.__died()
        self.current_actions.discard(Action.TakingDamage)

    @__do_nothing_if_dead
    def __died(self):
        self.is_alive = False
        self.frames[13] = pygame.transform.flip(Images.Robot[13], True, True)
        self.rect.y += self.rect.height - 10
        self.current_frame = 13
        if self.on_death:
            self.on_death()

    @__do_nothing_if_dead
    def __check_if_in_screen(self):
        if self.tile[0] > TILE_COLUMN_COUNT - 1:
            self.__died()

    @__do_nothing_if_dead
    def delay(self, time, is_player_delay=False):
        self.__delay_timer = time
        self._is_player_delay = is_player_delay

        if is_player_delay:
            self.current_actions.add(Action.Delay)

    def __handle_delay(self):
        self.__delay_timer -= 1
        if not self.__delay_timer and self._is_player_delay:
            self.current_actions.discard(Action.Delay)

    @__do_nothing_if_dead
    def set_in_action(self, in_action):
        if in_action:
            self.in_action = in_action

    @__do_nothing_if_dead
    def __handle_action_finished(self):
        if not self.in_action or len(self.current_actions):
            return

        self.in_action = False

        if self.on_action_finished:
            self.on_action_finished()
