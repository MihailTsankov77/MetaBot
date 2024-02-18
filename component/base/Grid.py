import pygame

from consts.game import TILE_ROW_COUNT, TILE_SIZE, TILE_COLUMN_COUNT


class Grid:

    def __init__(self, screen, visible_rows=[1]):
        self.screen = screen

        self.grid = []
        for i in range(TILE_ROW_COUNT):
            self.grid.append([])
            if visible_rows == None or i in visible_rows:
                for j in range(TILE_COLUMN_COUNT):
                    self.grid[i].append(pygame.Rect(
                        j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def update(self):
        for row in self.grid:
            for tile in row:
                pygame.draw.rect(self.screen, (255, 200, 200), tile, 2)
