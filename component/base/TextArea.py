import pygame


class TextArea:
    font_size = 20
    font_family = 'arial'
    text_color = (0, 0, 0)
    padding_horizontal = 10

    show_cursor = True
    show_border = True

    def __init__(self, screen, position, size):
        self.screen = screen
        self.rows = [''] 
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.position = (position[0] + self.padding_horizontal, position[1] + self.padding_horizontal)
        self.rect = pygame.Rect(position, size)

    def handle_input(self, event):
        if event.type == pygame.TEXTINPUT:
            self.rows[-1] += event.text
            row_width = self.font.render(self.rows[-1], True, self.text_color).get_width()
            if row_width>= self.rect.width - 2 * self.padding_horizontal - 5:
                self.rows.append('')
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.rows.append('')
            elif event.key == pygame.K_BACKSPACE:
                self.rows[-1] = self.rows[-1][:-1]
                if len(self.rows[-1]) == 0:
                    if len(self.rows) > 1:
                        self.rows = self.rows[:-1]
    
    def get_text(self):
        return '\n'.join(self.rows)
    
    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, self.text_color)
        self.screen.blit(text_surface, position)
        
    def draw(self):
        if self.show_border:
            pygame.draw.rect(self.screen, self.text_color, self.rect, 2)

        for i, row in enumerate(self.rows):
            self.draw_text(row, (
                self.position[0], 
                self.position[1] + i * self.font_size
                ))

        if self.show_cursor:
            cursor_x = self.font.render(self.rows[-1], True, self.text_color).get_width() + self.position[0] + 2
            cursor_y = self.position[1] + (len(self.rows) - 1) * self.font_size
            pygame.draw.line(self.screen, self.text_color, (cursor_x, cursor_y), (cursor_x, cursor_y + self.font_size))
            