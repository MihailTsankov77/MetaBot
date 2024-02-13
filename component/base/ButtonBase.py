import pygame

class ButtonBase:

    def __init__(self, screen, component, on_click, on_hover=None):
        self.component = component
        self.on_click = on_click
        self.screen = screen
        self.on_hover = on_hover
    
    def draw(self):
        pos = pygame.mouse.get_pos()

        if self.component.rect.collidepoint(pos):
            if self.on_hover is not None:
                self.on_hover()
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.on_click()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        self.component.draw()