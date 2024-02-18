from levels.players.BasePlayer import BasePlayer
from text_parsers.from_file_to_text.annotations import visible


class Player_level_3(BasePlayer):
    distance = 0

    def __init__(self,  x, health, robot):
        super().__init__(x, health, robot)
        self.x = x
        self.health = health

    def __getattribute__(self, __name):
        if __name == 'take_damage' or __name == '_move':
            self._trigger_action = True
        return super().__getattribute__(__name)

    def _sync(self):
        self._base_x = self.x
        self._base_health = self.health

    @visible
    def _move(self):
        self.x += 2

    @visible
    def take_damage(self, damage):
        self.health -= damage
