


def build_commands_string(commands, player_name, current_command):

    string_commands = [f'{player_name}.{command}()' for command in commands]

    for i in range(len(string_commands)):
        if i < current_command:
            string_commands[i] = f'<font color=#FF0000>{string_commands[i]}</font>'
            continue
        if i == current_command:
            string_commands[i] = f'<font color=#00FF00>{string_commands[i]}</font>'

    return '\n'.join(string_commands)