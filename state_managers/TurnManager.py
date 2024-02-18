from text_parsers.commands.commands_string_builder import build_commands_string
from consts.game import PLAYER_NAME, SECOND


class TurnManager:
    def __init__(self, player,
                 update_commands,
                 commands,
                 player_name=PLAYER_NAME,
                 delay_player=None,
                 on_command_finished=None):
        self.player = player
        self.commands = commands
        self.update_commands = update_commands
        self.current_command = -1
        self.player_name = player_name
        self.delay_player = delay_player
        self.on_command_finished = on_command_finished

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
            self.on_command_finished()
            return

        self.__call_command(self.commands[self.current_command])

    def __call_command(self, command):
        method_name, *raw_params = command
        params = [param for param in raw_params if param]
        method = getattr(self.player, method_name, None)
        if method:
            if params:
                return method(*params)
            return method()

    def next_turn(self):
        if self.delay_player and self.current_command >= 0:
            self.delay_player(SECOND)

        self.__execute_command()
