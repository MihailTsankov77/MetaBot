
def _get_params_string(params):
    filtered_params = [str(param) for param in params if param]
    return f"({', '.join(filtered_params) if filtered_params else ''})"


def build_commands_string(commands, player_name, current_command):
    string_commands = [f"{player_name}.{name}{_get_params_string(params)}"
                       for name, *params in commands]

    for i in range(len(string_commands)):
        if i < current_command:
            string_commands[i] = f'<font color=#FF0000>{string_commands[i]}</font>'
            continue
        if i == current_command:
            string_commands[i] = f'<font color=#00FF00>{string_commands[i]}</font>'

    return '\n'.join(string_commands)
