import pygame

from consts.game import FPS, GATE_SIZE, TILE_SIZE
from images.image_loader.images import Images


class AssertGate:
    size = (GATE_SIZE, GATE_SIZE)
    timer = FPS * 3

    show_hitbox = True

    def __init__(self, screen, position, player, check_condition, on_fail=None, on_pass=None):
        self.screen = screen
        self.check_condition = check_condition
        self.on_fail = on_fail
        self.on_pass = on_pass
        self.player = player

        self.image =  pygame.transform.scale(Images.Gate, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        hitbox_size = (TILE_SIZE, GATE_SIZE)
        self.hitbox = pygame.Rect(0, 0, *hitbox_size)
        self.hitbox.center = self.rect.center
        

        self.current_timer = 0
        self.checked = False

    def wait_for_condition(self):
        if self.checked:
            return
        
        self.current_timer += 1
        if self.current_timer > self.timer:
            self.checked = True
            if self.check_condition(self.player):
                self.on_pass()
            else:
                self.on_fail()

    def draw(self):
        self.screen.blit(self.image, self.rect)

        if self.show_hitbox:
            pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)

        if self.hitbox.colliderect(self.player.rect):
            self.wait_for_condition()
        else:
            self.current_timer = 0
