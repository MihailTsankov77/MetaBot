import pygame

from component.backgrounds.MenuBackground import MenuBackground
from component.buttons.TextButton import TextButton
from component.Gear.GearMouse import GearMouse
from consts.game import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS


class Restart:
    def __init__(self, screen):
        self.screen = screen
        self.background = MenuBackground(screen)
        self.mouse = GearMouse.get_instance(screen)
        self.restart_button = TextButton(screen,
                                         'Loser! Try again!',
                                         (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                                         text_color=(250, 0, 20))

    def set_on_button_press(self, on_button_press):
        self.restart_button.set_on_click(on_button_press)

    def __update(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.restart_button.update()
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
