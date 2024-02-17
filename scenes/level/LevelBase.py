import pygame
import pygame_gui

from component.backgrounds.LevelBackground import LevelBackground
from component.base.TextArea import TextArea
from component.base.Grid import Grid
from component.base.Text import Text
from component.Gear.GearButton import GearButton
from state_managers.TurnManager import TurnManager
from component.buttons.TextButton import TextButton
from consts.game import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_NAME

from text_parsers.from_text_to_code.text_parser import to_code
from text_parsers.from_text_to_code.PlayerDieException import PlayerDieException


class LevelBase:
    draw_grid = True

    descriptionText = "Spikes deal 1 dmg\nGoblins deal 3 dmg\nBombs deal 2 dmg"

    def __init__(self, screen, code, manager, player, commands, on_fail, on_command_finished = None, player_name = PLAYER_NAME):
        self.screen = screen
        self.manager = manager

        self.grid = Grid(screen)
        self.background = LevelBackground(screen)

        area_size = (SCREEN_WIDTH // 7 * 2, SCREEN_HEIGHT - self.background.height)
        textarea_size = (SCREEN_WIDTH - 2 * area_size[0], area_size[1])

        area_y = self.background.height

        textarea_position = (area_size[0], area_y)
        self.textarea = TextArea(screen, textarea_position, textarea_size)

        pygame_gui.elements.UITextBox(
            html_text=code,
            relative_rect=pygame.Rect((0, area_y), area_size),
            manager=manager)
        
        self.commandsTile = pygame_gui.elements.UITextBox(
            html_text='',
            relative_rect=pygame.Rect((area_size[0] + textarea_size[0], area_y), area_size),
            manager=manager)
        
        self.description = Text(screen, self.descriptionText, (10, 0))


        self.turn_manager = TurnManager(player, self.set_commands, commands, delay_player=player._set_delay, on_command_finished=on_command_finished, player_name=player_name)

        player._set_on_action_finished(self.turn_manager.next_turn)

        self.player = player
        self.player_name = player_name
        self.__on_fail = on_fail

        self.start_button = GearButton(screen, 200, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100), self.__on_start)
        self.__is_started = False

        self.back_button = TextButton(screen, 'BACK', (SCREEN_WIDTH - 50, 20), font_size=20, hover_color=(0, 200, 20))

    def set_on_back(self, on_back):
        self.back_button.set_on_click(on_back)

    def __handle_text_to_code(self):
        try:
            to_code(self.get_code(), {self.player_name: self.player})   
            return True
        except PlayerDieException as e:
            print(e)
            self.__on_fail()
            return False

    def __on_start(self):
        if self.__is_started:
            return
        
        if not self.__handle_text_to_code():
            return
        self.__is_started = True
        self.turn_manager.next_turn()


    def handle_input(self, event):
        self.textarea.handle_input(event)

    def get_code(self):
        return self.textarea.get_text()
    
    def set_commands(self, commands):
        self.commandsTile.set_text(commands)

    def update(self):
        self.manager.draw_ui(self.screen)
        self.background.update()
        self.textarea.update()
        self.description.update()
        self.start_button.update()
        self.back_button.update()

        if self.draw_grid:
            self.grid.update()
