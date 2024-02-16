import pygame

from consts.game import FPS, GATE_SIZE, TILE_SIZE, TILE_COLUMN_COUNT
from images.image_loader.images import Images
from utils.coordinates import get_coordinates_from_grid
from utils.collision import are_colliding

class AssertGate:
    size = (GATE_SIZE, GATE_SIZE)
    timer = FPS * 3

    def __init__(self, screen, player, check_condition, tile = (TILE_COLUMN_COUNT -1, 2), on_fail=None, on_pass=None):
        self.screen = screen
        self.check_condition = check_condition
        self.on_fail = on_fail
        self.on_pass = on_pass
        self.player = player

        self.image =  pygame.transform.scale(Images.Gate, self.size)
        self.rect = self.image.get_rect()

        self.tile = tile
    
        self.rect.topleft = self.coordinates        

        self.current_timer = 0
        self.checked = False
    
    @staticmethod
    def get_coordinates(tile):
        return get_coordinates_from_grid(tile, TILE_SIZE, (-GATE_SIZE / 10, -GATE_SIZE / 5))

    @property
    def coordinates(self):
        return  AssertGate.get_coordinates(self.tile)

    def __wait_for_condition(self):
        if self.checked:
            return
        
        self.current_timer += 1
        if self.current_timer > self.timer:
            self.checked = True
            if self.check_condition(self.player):
                self.on_pass()
            else:
                self.on_fail()

    @property
    def __is_colliding_with_player(self):
        return are_colliding(self.rect, self.player.rect)

    def draw(self):
        self.screen.blit(self.image, self.rect)

        

        if self.__is_colliding_with_player:
            self.__wait_for_condition()
        else:
            self.current_timer = 0
