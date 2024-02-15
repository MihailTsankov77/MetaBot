import pygame

from consts.game import FPS
from component.Gear.GearButton import GearButton
from component.Gear.GearMouse import GearMouse
from component.Robot.Robot import Robot
from component.AssertGate.AssertGate import AssertGate
from component.base.Grid import Grid
from component.base.TextArea import TextArea

pygame.init()

BG = (255, 255, 255)



class Main:
    def __init__(self, screen, UI_manager):
        self.screen = screen
        self.mouse = GearMouse.get_instance(screen)
        self.manager = UI_manager 

       
        self.robot = Robot(screen, tile=(7.3, 2))

        self.grid = Grid(screen)

        self.assertGate = AssertGate(screen, 
                                     self.robot, 
                                     lambda robot: True, 
                                     tile=(8, 2),
                                     on_fail=lambda: print("Fail"), 
                                     on_pass=lambda: print("Pass")
                                     )

        self.gear = GearButton(screen, 100, (100, 100), lambda: self.robot.move_tile())

        self.textarea = TextArea(screen)

    def __call__(self):
        clock = pygame.time.Clock()

        while True:
            time_delta = clock.tick(FPS)/1000.0

            for event in pygame.event.get():
                self.textarea.handle_input(event)
                if event.type == pygame.QUIT:
                    return

            self.screen.fill(BG)


            self.grid.draw()

            self.gear.draw()

            self.textarea.draw()
          
            self.assertGate.draw()

            self.robot.draw()
            self.mouse.draw()
            pygame.display.update()