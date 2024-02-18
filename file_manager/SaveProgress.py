from datetime import datetime

from file_manager.FileManager import FileManager


class SaveProgress:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.file_manager = FileManager()

    def save_level(self, level):
        text = f'{level} {datetime.now()}\n'
        self.file_manager.save_progress_write(text)

    def get_completed_levels(self):
        text = self.file_manager.save_progress_read()
        return list(set(map(lambda x: int(x.split(' ')[0]), filter(lambda x: x != '', text.split('\n')))))
