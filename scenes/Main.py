import pygame

from consts.game import FPS
from component.Gear.GearButton import GearButton
from component.Gear.GearMouse import GearMouse
from component.Robot.Robot import Robot
from component.AssertGate.AssertGate import AssertGate
from scenes.LevelBase import LevelBase

pygame.init()

class Main:
    def __init__(self, screen, UI_manager):
        self.screen = screen
        self.mouse = GearMouse.get_instance(screen)
        self.manager = UI_manager 

        self.level = LevelBase(screen, (
            'Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>', 
            'Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>'
            ), self.manager)
       
        self.robot = Robot(screen, tile=(7.3, 1))

        self.assertGate = AssertGate(screen, 
                                     self.robot, 
                                     lambda robot: True, 
                                     tile=(8, 1),
                                     on_fail=lambda: print("Fail"), 
                                     on_pass=lambda: print("Pass")
                                     )

        self.gear = GearButton(screen, 100, (100, 100), lambda: self.robot.move_tile())


    def __drew_entities(self):
        self.gear.draw()          
        self.assertGate.draw()
        self.robot.draw()


    def __call__(self):
        clock = pygame.time.Clock()

        while True:
            time_delta = clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                self.level.handle_input(event)
                self.manager.process_events(event)

            self.level.draw()

            self.__drew_entities()

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)
            self.mouse.draw()
            pygame.display.update()