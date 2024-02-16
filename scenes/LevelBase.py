import pygame
import pygame_gui

from component.base.Background import Background
from component.base.TextArea import TextArea
from component.base.Grid import Grid
from consts.game import SCREEN_WIDTH, SCREEN_HEIGHT


class LevelBase:
    draw_grid = True

    def __init__(self, screen, levelConfig, manager):
        self.screen = screen
        implementation, commands = levelConfig

        self.grid = Grid(screen)
        self.background = Background(screen)

        area_size = (SCREEN_WIDTH // 7 * 2, SCREEN_HEIGHT - self.background.height)
        textarea_size = (SCREEN_WIDTH - 2 * area_size[0], area_size[1])

        area_y = self.background.height

        textarea_position = (area_size[0], area_y)
        self.textarea = TextArea(screen, textarea_position, textarea_size)

        pygame_gui.elements.UITextBox(
            html_text=implementation,
            relative_rect=pygame.Rect((0, area_y), area_size),
            manager=manager)
        
        pygame_gui.elements.UITextBox(
            html_text=commands,
            relative_rect=pygame.Rect((area_size[0] + textarea_size[0], area_y), area_size),
            manager=manager)

    def handle_input(self, event):
        self.textarea.handle_input(event)

    def get_text(self):
        return self.textarea.get_text()

    def draw(self):
        self.background.draw()
        self.textarea.draw()

        if self.draw_grid:
            self.grid.draw()
