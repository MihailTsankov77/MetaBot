from text_parsers.commands.commands_string_builder import build_commands_string
from consts.game import PLAYER_NAME, SECOND

class TurnManager:
    def __init__(self, players, update_commands, commands, player_name = PLAYER_NAME, delay_player = None):
        self.players = players
        self.commands = commands
        self.update_commands = update_commands
        self.current_command = -1
        self.player_name = player_name
        self.delay_player = delay_player
        
        self.__update_commands()

    @property
    def __commands_text(self):
        return build_commands_string(self.commands, self.player_name, self.current_command)
    
    def __update_commands(self):
        self.update_commands(self.__commands_text)
    
    def __execute_command(self):
        self.current_command += 1    
        self.__update_commands()

        if self.current_command >= len(self.commands):
            return

        method = getattr(self.players, self.commands[self.current_command])
        if method:
            method()

    def next_turn(self):
        if self.delay_player:
            self.delay_player(SECOND // 2)

        self.__execute_command()



