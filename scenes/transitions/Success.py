import pygame

from component.backgrounds.MenuBackground import MenuBackground
from component.buttons.TextButton import TextButton
from component.Gear.GearMouse import GearMouse
from consts.game import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS


class Success:
    def __init__(self, screen, on_button_press):
        self.screen = screen
        self.background = MenuBackground(screen)
        self.mouse = GearMouse.get_instance(screen)
        self.success_button = TextButton(screen,
                                         'Hooraaay! You did it!',
                                         (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                                         text_color=(0, 200, 20),
                                         on_click=on_button_press,
                                         hover_color=(200, 0, 200))

    def __update(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.success_button.update()
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
        self.__init()
