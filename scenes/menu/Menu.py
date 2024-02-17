import pygame

from component.backgrounds.MenuBackground import MenuBackground
from component.buttons.TextButton import TextButton
from component.Gear.GearMouse import GearMouse
from consts.game import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS

class Menu:
    def __init__(self, screen, open_choose_level):
        self.screen = screen
        self.background = MenuBackground(screen)
        self.mouse = GearMouse.get_instance(screen)
        self.start_button = TextButton(screen, 
                                       'START THE GAME', 
                                       (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 
                                       open_choose_level,
                                       hover_color=(200, 0, 200)                                       
                                       )

    def __update(self):
        self.background.update()
        self.start_button.update()
        self.mouse.update()
        pygame.display.update()

    def __init(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.__update()

    def __call__(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.__init()