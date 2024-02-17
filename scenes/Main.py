from scenes.level.Level import Level
from scenes.menu.Menu import Menu
from scenes.menu.ChooseLevel import ChooseLevel

class Main:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager

        self.start_level = Level(screen, manager)
        self.show_choose_level = ChooseLevel(screen, self.start_level)

        self.start_level.set_on_back(self.show_choose_level)

        self.show_menu = Menu(screen, self.show_choose_level)
        self.show_choose_level.set_on_back(self.show_menu)

    def __call__(self):
        self.show_menu()
