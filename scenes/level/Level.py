import pygame

from component.Gear.GearMouse import GearMouse
from component.Robot.Robot import Robot
from component.AssertGate.AssertGate import AssertGate
from scenes.level.LevelBase import LevelBase
from consts.game import FPS, BACKGROUND_COLOR

pygame.init()

# TODO 
player_commands = [
    ('move_tile', None),
    ('move_tile', None),
    ('take_damage', 1),
    ('move_tile', None),
    ('take_damage', 10),
    ('move_tile', None),
]

class Level:
    def __init__(self, screen, UI_manager):
        self.screen = screen
        self.mouse = GearMouse.get_instance(screen)
        self.manager = UI_manager 

        self.robot = Robot(screen, tile=(1, 1), 
                           health=10, 
                           on_death=lambda: print("Robot is dead"))

        self.level = LevelBase(
            screen, 
            'Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>',
            self.manager,
            player=self.robot,
            commands=player_commands
            )
       
        self.assertGate = AssertGate(screen, 
                                     self.robot, 
                                     lambda robot: True, 
                                     tile=(8, 1),
                                     on_fail=lambda: print("Fail"), 
                                     on_pass=lambda: print("Pass")
                                     )

    def set_on_back(self, on_back):
        self.level.set_on_back(on_back)

    def __update_entities(self):
        self.assertGate.update()
        self.robot.update()


    def __update(self, time_delta):
        self.mouse.update()
        self.manager.update(time_delta)
        pygame.display.update()

    def __init(self):
        clock = pygame.time.Clock()

        while True:
            time_delta = clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                self.level.handle_input(event)
                self.manager.process_events(event)

            self.level.update()
            self.__update_entities()
            self.__update(time_delta)

    def __call__(self, level):
        self.screen.fill(BACKGROUND_COLOR)
        self.__init()
              