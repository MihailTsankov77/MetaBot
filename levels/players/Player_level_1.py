from levels.players.BasePlayer import BasePlayer
from text_parsers.from_file_to_text.annotations import visible

class Player_level_1(BasePlayer):
    
    @visible
    def move(self):
        self.x += 1
    