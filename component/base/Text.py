import pygame

class Text:
    font_size = 20
    font_family = "arial"
    text_color = (255, 255, 255)


    def __init__(self, screen, text, position):
        self.screen = screen
        self.text = text
        self.position = position
        self.font = pygame.font.SysFont(self.font_family, self.font_size)

    def update(self):
        text = self.font.render(self.text, True, self.text_color)
        self.screen.blit(text, self.position)