import pygame

from component.Gear.GearMouse import GearMouse
from component.Robot.Robot import Robot
from component.AssertGate.AssertGate import AssertGate
from scenes.level.LevelBase import LevelBase
from scenes.transitions.Success import Success
from scenes.transitions.Restart import Restart
from consts.game import FPS, BACKGROUND_COLOR, SECOND
from levels.levels_config import levels_configs

pygame.init()

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

        level_config = levels_configs.get_level_config(2)

        self.player_health = level_config.player_health
        self.player_x = level_config.player_x

        self.robot = Robot(self.screen, tile=(self.player_x, 1), 
                           health= self.player_health, 
                           on_death = self.__on_fail)

        self.player = level_config.player_class(self.player_x, self.player_health, self.robot)

        self.no_more_commands_dead_timer = None
        self.run_out_of_commands = False
        def on_command_finished():
            self.no_more_commands_dead_timer = 2 * SECOND
            self.run_out_of_commands = True

        self.level = LevelBase(
            self.screen, 
            level_config.player_code,
            self.manager,
            player = self.player,
            on_fail=self.__on_fail,
            commands= level_config.player_commands,
            on_command_finished = on_command_finished
            )
        
        def on_step_on_assert_gate():
            self.no_more_commands_dead_timer = None

        def gate_condition(robot):
            return self.run_out_of_commands and level_config.check_condition(robot)
       
        self.assertGate = AssertGate(self.screen, 
                                     self.robot, 
                                     gate_condition, 
                                     tile=(level_config.assert_gate_x, 1),
                                     on_step = on_step_on_assert_gate,
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

    def __handle_end(self):
        if self.no_more_commands_dead_timer:
            self.no_more_commands_dead_timer -= 1
            if self.no_more_commands_dead_timer == 0:
                self.__on_fail()

    def __update_entities(self):
        self.assertGate.update()
        self.player._update()

    def __update(self, time_delta):
        self.__handle_end()
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
              