import pygame


class TextArea:
    font_size = 20
    font_family = 'arial'
    text_color = (0, 0, 0)

    def __init__(self, screen):
        self.screen = screen
        self.rows = [] #["1."]
        self.font = pygame.font.SysFont(self.font_family, self.font_size)

    def handle_input(self, event):
        if event.type == pygame.TEXTINPUT:
            self.rows[-1] += event.text
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.rows.append('') #f"{len(self.rows) + 1}."
            elif event.key == pygame.K_BACKSPACE:
                self.rows[-1] = self.rows[-1][:-1]
                if len(self.rows[-1]) == 0:
                    if len(self.rows) > 1:
                        self.rows = self.rows[:-1]
    
    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, self.text_color)
        self.screen.blit(text_surface, position)
        
    def draw(self):
        for i, row in enumerate(self.rows):
            self.draw_text(row, (100, 400 + i * self.font_size))
            
        
