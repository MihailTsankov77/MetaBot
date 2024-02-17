from typing import Any
from levels.players.BasePlayer import BasePlayer
from text_parsers.from_file_to_text.annotations import visible
from math import floor


class Player_level_2(BasePlayer):
    distance = 0

    def __getattribute__(self, __name):
        if __name == 'change_distance':
            self._trigger_action = True
        return super().__getattribute__(__name)

    @visible
    def change_distance(self):
        self.distance = 1

    @visible
    def _move(self):
        self.x += floor(self.distance) # TODO fix this
    