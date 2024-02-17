import pygame

from consts.game import FPS
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

        self.robot = Robot(screen, tile=(8, 1), health=10, on_death=lambda: print("Robot is dead"))

        def robot_test():
            self.robot.move_tile()
            self.robot.take_damage(1)

        self.level = LevelBase(
            screen, 
            (
            'Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>', 
            'Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>'
            ), 
            self.manager,
            robot_test
            )
       
        self.assertGate = AssertGate(screen, 
                                     self.robot, 
                                     lambda robot: True, 
                                     tile=(8, 1),
                                     on_fail=lambda: print("Fail"), 
                                     on_pass=lambda: print("Pass")
                                     )


    def __drew_entities(self):
        self.assertGate.draw()
        self.robot.draw()


    def __update(self, time_delta):
        self.mouse.draw()
        self.manager.update(time_delta)
        pygame.display.update()


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

            self.__update(time_delta)
              