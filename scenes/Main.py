
from scenes.level.Level import Level
from scenes.menu.Menu import Menu

class Main:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager

        self.start_level = Level(screen, manager)

        self.show_menu = Menu(screen, lambda: self.start_level(1))

    def __call__(self):
        self.show_menu()
