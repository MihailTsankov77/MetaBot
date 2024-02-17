from  text_parsers.from_file_to_text.file_parser import parse_file
from levels.players.Player_level_1 import Player_level_1


def __get_code(level):
    with open(f'levels/players/Player_level_{level}.py', 'r') as file:
        return parse_file(file)
    

__level_1_config = {
"check_condition": lambda robot: True,
"player_health": 10,
"player_x": 2,
"assert_gate_x": 8,
"player_class": Player_level_1,
"player_code":__get_code(1),
"player_commands": [
    ('move', None),
    ('move', None),
    # ('take_damage', 1),
    # ('move', None),
    # ('take_damage', 10),
    # ('move', None),
]
}

# TODO make class


levels_configs = [__level_1_config]
