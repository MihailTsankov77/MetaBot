import pygame

from component.Gear.GearButton import GearButton
from component.Gear.GearMouse import GearMouse
from component.Robot.Robot import Robot
from consts.game import FPS
from component.AssertGate.AssertGate import AssertGate

pygame.init()

BG = (255, 255, 255)


class Main:
    def __init__(self, screen, UI_manager):
        self.screen = screen
        self.mouse = GearMouse.get_instance(screen)
        self.manager = UI_manager 

       
        self.robot = Robot(screen, (200, 200))

        self.assertGate = AssertGate(screen, 
                                     (300, 200), 
                                     self.robot, 
                                     lambda robot: True, 
                                     on_fail=lambda: print("Fail"), 
                                     on_pass=lambda: print("Pass")
                                     )

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
          
            self.assertGate.draw()

            self.robot.draw()
            self.mouse.draw()
            pygame.display.update()