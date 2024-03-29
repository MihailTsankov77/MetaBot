from levels.players.BasePlayer import BasePlayer
from text_parsers.from_file_to_text.annotations import visible


class Player_level_1(BasePlayer):

    def __init__(self,  x, health, robot):
        super().__init__(x, health, robot)
        self.x = x

    def __getattribute__(self, __name):
        if __name == 'move':
            self._trigger_action = True
        return super().__getattribute__(__name)

    def _sync(self):
        self._base_x = self.x

    @visible
    def move(self):
        self.x += 1
