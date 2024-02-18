from component.Gear.Gear import Gear
from component.base.ButtonBase import ButtonBase
from component.Gear.GearMouse import GearMouse


class GearButton:
    rotate_speed = 2
    mouse_rotate_speed = rotate_speed * -2

    def __init__(self, screen, size, position, on_click):
        self.gear = Gear(screen, size, position)
        gear_mouse = GearMouse.get_instance(screen)

        def on_hover():
            self.gear.rotate(self.rotate_speed)
            gear_mouse.rotate(self.mouse_rotate_speed)

        self.button = ButtonBase(screen, self.gear, on_click, on_hover)

    def update(self):
        self.button.update()
