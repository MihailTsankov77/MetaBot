import pygame

from component.Gear.Gear import Gear

  
class GearMouse:
    __instance = None

    def __init__(self, screen):
        pygame.mouse.set_visible(False)
        self.gear = Gear(screen, size=50, position=(0, 0))

    def rotate(self, speed):
        self.gear.rotate(speed)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.gear.set_position(mouse_pos)
        self.gear.draw()

    @staticmethod
    def get_instance(screen):
        if GearMouse.__instance is None:
            GearMouse.__instance = GearMouse(screen)
        return GearMouse.__instance
