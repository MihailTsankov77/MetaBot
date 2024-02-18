from levels.players.BasePlayer import BasePlayer
from text_parsers.from_file_to_text.annotations import visible


class Player_level_4(BasePlayer):
    health = 1

    def __init__(self,  x, health, robot):
        super().__init__(x, health, robot)
        self.x = x
        self.health = health

    def __getattribute__(self, __name):
        if __name == '_move':
            self._trigger_action = True
        return super().__getattribute__(__name)

    def _sync(self):
        self._base_x = self.x
        self._base_health = self.health

    @visible
    def _move(self):
        self.x += 6
