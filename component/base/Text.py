import pygame

class Text:
    font_family = "arial"
    text_color = (255, 255, 255)

    def __init__(self, screen, text, position, font_size = 20, centered = False):
        self.screen = screen
        self.text = text
        self.position = position
        self.font_size = font_size
        self.set_font_color(self.text_color)
        if centered:
            self.position = (self.position[0] - self.rect.width // 2, self.position[1] - self.rect.height // 2)        

    def update(self):
        text = self.font.render(self.text, True, self.text_color)
        self.screen.blit(text, self.position)

    def set_font_color(self, color):
        self.text_color = color
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.rect = self.font.render(self.text, True, self.text_color).get_rect()
        self.rect.topleft = self.position
