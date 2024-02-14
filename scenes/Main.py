import pygame

from component.Gear.GearButton import GearButton
from component.Gear.GearMouse import GearMouse
from component.Robot.Robot import Robot

pygame.init()

BG = (255, 255, 255)
FPS = 60

class Main:
    def __init__(self, screen, UI_manager):
        self.screen = screen
        self.mouse = GearMouse.get_instance(screen)
        self.manager = UI_manager 

       
        self.robot = Robot(screen, (200, 200))

        self.gear = GearButton(screen, 100, (100, 100), lambda: self.robot.move_tile())

    def __call__(self):
        clock = pygame.time.Clock()

        while True:
            time_delta = clock.tick(FPS)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.screen.fill(BG)
            self.gear.draw()
            self.robot.draw()



            self.mouse.draw()
            pygame.display.update()