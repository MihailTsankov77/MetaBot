from datetime import datetime

from file_manager.FileManager import FileManager

class SaveProgress:

    def __init__(self, path_to_base):
        self.__path_to_base = ''
        self.file_manager = FileManager()
        self.__path_to_base = path_to_base

    def save_level(self, level):
        text = f'{level} {datetime.now()}\n'

        self.file_manager.save_progress_write(self.__path_to_base, text)
    
    def get_completed_levels(self):
        text = self.file_manager.save_progress_read(self.__path_to_base)
        return list(set(map(lambda x: int(x.split(' ')[0]), filter(lambda x: x != '', text.split('\n')))))