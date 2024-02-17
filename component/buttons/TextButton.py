from component.base.Text import Text
from component.base.ButtonBase import ButtonBase

class TextButton:
    rotate_speed = 2
    mouse_rotate_speed = rotate_speed * -2

    def __init__(self, 
                 screen, 
                 text, 
                 position, 
                 on_click = None, 
                 font_size = 40, 
                 hover_color = (0, 0, 0), 
                 text_color = (255, 255, 255)):
        self.text = Text(screen, text, position, font_size, centered=True)
        self.hover_color = hover_color
        self.text_color = text_color
        def on_hover():
            self.text.set_font_color(self.hover_color)
        
        def on_unHover():
            self.text.set_font_color(self.text_color)
       
        self.button = ButtonBase(screen, self.text, on_click, on_hover, on_unHover)

    def set_on_click(self, on_click):
        self.button.on_click = on_click

    def set_color(self, color):
        self.text_color = color
        self.text.set_font_color(color)

    def update(self):
        self.button.update()