import pygame

from text_parsers.commands.commands_string_builder import build_commands_string
from consts.game import PLAYER_NAME

class TurnManager:
    def __init__(self, players, update_commands, commands, player_name = PLAYER_NAME):
        self.players = players
        self.commands = commands
        self.update_commands = update_commands
        self.current_command = -1
        self.player_name = player_name
        
        self.__update_commands()

    @property
    def __commands_text(self):
        return build_commands_string(self.commands, self.player_name, self.current_command,)
    
    def __update_commands(self):
        self.update_commands(self.__commands_text)

    def next_turn(self):
        pygame.time.delay(200)
        
        self.current_command += 1
        if self.current_command >= len(self.commands):
            return
        
        self.__update_commands()

        method = getattr(self.players, self.commands[self.current_command])
        if method:
            method()


