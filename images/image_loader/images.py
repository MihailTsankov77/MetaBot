import pygame

class Images_Loader:
    path = "images/assets/"
    assets = {
        "Gear": "gear.png"
    }
    def __init__(self):
       for key, value in self.assets.items():
           setattr(self, key, pygame.image.load(self.path + value))


Images = Images_Loader()