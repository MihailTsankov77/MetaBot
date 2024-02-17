import pygame

from file_manager.SaveProgress import SaveProgress

from component.backgrounds.MenuBackground import MenuBackground
from component.buttons.TextButton import TextButton
from component.Gear.GearMouse import GearMouse
from consts.game import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_COUNT, BACKGROUND_COLOR, FPS

class ChooseLevel:
    def __init__(self, screen, start_level):
        self.screen = screen
        self.background = MenuBackground(screen)
        self.mouse = GearMouse.get_instance(screen)

        def choose_level(level):
            self.is_running = False
            start_level(level)

        self.level_texts = []
        for i in range(LEVEL_COUNT):
            self.level_texts.append(
                TextButton(screen, 
                           f'Level {i + 1}', 
                           (i % 5 * 150 + 300, i // 5 * 100 + SCREEN_HEIGHT // 2 - 100), 
                           lambda: choose_level(i),
                           font_size=30,
                           hover_color=(200, 0, 200)))
            
        self.back_button = TextButton(screen, 'BACK', (SCREEN_WIDTH - 50, 20), font_size=20, hover_color=(0, 200, 20))

        self.is_running = True

    def set_on_back(self, on_back):
        def _on_back():
            self.is_running = False
            on_back()
        self.back_button.set_on_click(_on_back)
      
    def __update(self):
        self.background.update()
        self.back_button.update()
    
        for text in self.level_texts:
            text.update()

        self.mouse.update()
        pygame.display.update()

    def __init(self):
        clock = pygame.time.Clock()

        while self.is_running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.__update()

    def __call__(self):
        self.is_running = True
        self.screen.fill(BACKGROUND_COLOR)
        completed_levels = [] #SaveProgress('..../').get_completed_levels() # TODO fix path
        for i in completed_levels:
            self.level_texts[i - 1].set_color((0, 255, 0))

        self.__init()