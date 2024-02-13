from component.Gear.Gear import Gear
from component.base.ButtonBase import ButtonBase

class GearButton:

    def __init__(self, screen, size, position, on_click):
        self.gear = Gear(screen, size, position)
        on_hover = lambda: self.gear.rotate(2)
        self.button = ButtonBase(screen, self.gear, on_click, on_hover)

    def draw(self):
        self.button.draw()