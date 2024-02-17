import pygame

class ButtonBase:

    def __init__(self, screen, component, on_click = None, on_hover=None, on_unHover=None):
        self.component = component
        self.on_click = on_click
        self.screen = screen
        self.on_hover = on_hover
        self.on_unHover = on_unHover
        self.clicked = False
    
    def update(self):
        if self.on_click is None:
            return

        pos = pygame.mouse.get_pos()

        if self.component.rect.collidepoint(pos):
            if self.on_hover is not None:
                self.on_hover()
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                if self.on_click is not None:
                    self.on_click()
        else:
            if self.on_unHover is not None:
                self.on_unHover()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        self.component.update()