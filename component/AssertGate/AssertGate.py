import pygame

from consts.game import FPS
from images.image_loader.images import Images


class AssertGate:
    size = (300, 300)
    timer = FPS * 3

    show_hitbox = False

    def __init__(self, screen, position, player, check_condition, on_fail=None, on_pass=None):
        self.screen = screen
        self.check_condition = check_condition
        self.on_fail = on_fail
        self.on_pass = on_pass
        self.player = player

        self.image =  pygame.transform.scale(Images.Gate, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width / 3, self.rect.height / 1.5)
        #  position is for bottom center of the rectage
        self.hitbox.center = position
        

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
