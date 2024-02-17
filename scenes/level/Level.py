import pygame

from component.Gear.GearMouse import GearMouse
from component.Robot.Robot import Robot
from component.AssertGate.AssertGate import AssertGate
from scenes.level.LevelBase import LevelBase
from scenes.transitions.Success import Success
from scenes.transitions.Restart import Restart
from levels.Player import Player
from consts.game import FPS, BACKGROUND_COLOR, SECOND

pygame.init()

# TODO 
player_commands = [
    ('move', None),
    # ('move', None),
    # ('take_damage', 1),
    # ('move', None),
    # ('take_damage', 10),
    # ('move', None),
]

class Level:
    def __init__(self, screen, UI_manager):
        self.screen = screen
        self.manager = UI_manager 
        self.__base_init()

    def __base_init(self):
        self.mouse = GearMouse.get_instance(self.screen)
        self.show_success =  Success(self.screen, lambda: print('TODO'))
        self.show_restart = Restart(self.screen)
        self._restart_timer = 0
        self._success_timer = 0

        self.player_health = 10
        self.player_x = 8

        self.robot = Robot(self.screen, tile=(self.player_x, 1), 
                           health=self.player_health, 
                           on_death = self.__on_fail)

        self.player = Player(self.player_x, self.player_health, self.robot)

        self.level = LevelBase(
            self.screen, 
            'Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>',
            self.manager,
            player = self.player,
            commands=player_commands,
            on_command_finished = self.__on_fail # TODO if you are on the assert gate just turn flag up and then check it here
            )
       
        self.assertGate = AssertGate(self.screen, 
                                     self.robot, 
                                     lambda robot: True, 
                                     tile=(8, 1),
                                     on_pass = self.__on_success,
                                     on_fail = self.__on_fail)


    def __on_fail(self):
        self._restart_timer = SECOND
        self._success_timer = 0
    
    def __on_success(self):
        self._success_timer = 1
        self._restart_timer = 0
    
    def __handle_transitions(self):
        ans = self.__handle_transition('_restart_timer')
        if ans != 0:
            return ans
        return self.__handle_transition('_success_timer')        
    
    def __handle_transition(self, transition):
        val = getattr(self, transition)
        if val > 0:
            setattr(self, transition, val - 1)
            if val - 1 == 0:
                if transition == '_success_timer':
                    self.show_success()
                else:
                    self.show_restart()
                return 2
            return 1
        return 0

    def set_on_back(self, on_back):
        self.level.set_on_back(on_back)

    def __update_entities(self):
        self.assertGate.update()
        
        self.player._update()

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
            
            if self.__handle_transitions() == 2:
                return
            
            self.level.update()
            self.__update_entities()
            self.__update(time_delta)

    def __call__(self, level):
        self.screen.fill(BACKGROUND_COLOR)
        self.__base_init()
        self.show_restart.set_on_button_press(lambda: self.__call__(level))
        self.__init()
              