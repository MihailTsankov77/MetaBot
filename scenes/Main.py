import pygame
import pygame_gui

from component.Gear.GearButton import GearButton
from component.Gear.GearMouse import GearMouse
from component.base.TextArea import TextArea

pygame.init()

BG = (0, 0, 0)
FPS = 60

class Main:
    def __init__(self, screen, UI_manager):
        self.screen = screen
        self.mouse = GearMouse.get_instance(screen)
        self.manager = UI_manager 

        self.textArea = TextArea()
        self.gear = GearButton(screen, 100, (100, 100), lambda: print("Clicked"))



    def __call__(self):
        clock = pygame.time.Clock()

        hello_button = pygame_gui.elements.UITextBox(
            html_text='Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>',
            relative_rect=pygame.Rect((350, 275), (200, 500)),
            manager=self.manager)

        while True:
            time_delta = clock.tick(FPS)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                         print('Hello World!')

                self.manager.process_events(event)


            self.screen.fill(BG)
            self.gear.draw()

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            self.mouse.draw()
            pygame.display.update()