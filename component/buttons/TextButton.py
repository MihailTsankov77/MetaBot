from component.base.Text import Text
from component.base.ButtonBase import ButtonBase

class TextButton:
    rotate_speed = 2
    mouse_rotate_speed = rotate_speed * -2

    def __init__(self, screen, text, position, on_click, font_size = 40):
        self.text = Text(screen, text, position, font_size)
        def on_hover():
            self.text.set_font_color((200, 0, 0))
        
        def on_unHover():
            self.text.set_font_color((255, 255, 255))
       
        self.button = ButtonBase(screen, self.text, on_click, on_hover, on_unHover)

    def update(self):
        self.button.update()