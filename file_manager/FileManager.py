


def _write_file(file_path, text_data):
    with open(file_path, 'a+') as file:
        file.write(text_data)

class FileManager:
    base_path = 'file_manager/files/'
    type_texts = ['save_progress']

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        for type_text in self.type_texts:
            path = f'{self.base_path}{type_text}.txt'
            def __write_file(path_to_base, text_data):
                _write_file(f'{path_to_base}{path}', text_data)
            setattr(self, f'{type_text}_write', __write_file)

            def __read_file(path_to_base):
                with open(f'{path_to_base}{path}', 'r') as file:
                    return file.read()
            setattr(self, f'{type_text}_read', __read_file)
