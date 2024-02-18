from text_parsers.from_file_to_text.file_parser import parse_file


class _LevelConfig:
    def __init__(self, level, check_condition, player_health, player_x, assert_gate_x, player_commands):
        self.level = level
        self.check_condition = check_condition
        self.player_health = player_health
        self.player_x = player_x
        self.assert_gate_x = assert_gate_x
        class_name = f'Player_level_{level}'
        self.player_class = __import__(f'levels.players.{class_name}', fromlist=[
                                       class_name]).__dict__[class_name]
        self.player_code = self.__get_code(level)
        self.player_commands = player_commands

    @staticmethod
    def __get_code(level):
        with open(f'levels/players/Player_level_{level}.py', 'r') as file:
            return parse_file(file)


class __LevelsConfigs:
    def __init__(self):
        self.levels_configs = []

    def add_level_config(self, level, check_condition, player_x, player_health, assert_gate_x, player_commands):
        self.levels_configs.append(_LevelConfig(
            level, check_condition, player_health, player_x, assert_gate_x, player_commands))

    def get_level_config(self, level):
        if level > len(self.levels_configs):
            return self.levels_configs[len(self.levels_configs) - 1]
        return self.levels_configs[level - 1]


levels_configs = __LevelsConfigs()


levels_configs.add_level_config(
    1,
    lambda _: True,
    2, 1,
    8,
    [
        ('move', None),
        ('move', None),
    ]
)

levels_configs.add_level_config(
    2,
    lambda _: True,
    1, 1,
    8,
    [
        ('change_distance', None),
        ('_move', None),
        ('change_distance', None),
        ('_move', None),
        ('change_distance', None),
        ('_move', None),
    ]
)

levels_configs.add_level_config(
    3,
    lambda robot: robot.health == 10,
    2, 10,
    8,
    [
        ('_move', None),
        ('take_damage', (30)),
        ('_move', None),
        ('take_damage', (999)),
        ('_move', None),
    ]
)
