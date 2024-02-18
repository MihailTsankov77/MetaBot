import pygame


class Images_Loader:
    path = "images/assets/"
    assets = {
        "Gear": {
            "asset": "gear.png",
            "is_image": True
        },
        "Robot": {
            "asset": "robot.png",
            "is_image": False,
            "size": (128, 128.33),
            "rows": 4,
            "columns": 5,
            "all_frames": 17
        },
        "LevelBackground": {
            "asset": "level_background.png",
            "is_image": True
        },
        "MenuBackground": {
            "asset": "menu_background.png",
            "is_image": True
        },
        "Gate": {
            "asset": "gate.png",
            "is_image": True
        },
        "Spikes": {
            "asset": "spikes.png",
            "is_image": True
        },
    }

    def __init__(self):
        for name, config in self.assets.items():
            if config['is_image']:
                setattr(self, name, pygame.image.load(
                    self.path + config['asset']))
            else:
                setattr(self, name, self.load_sprite_sheet(config))

    @staticmethod
    def load_sprite_sheet(config):
        sprite_sheet = pygame.image.load(Images_Loader.path + config['asset'])
        size = config['size']
        rows = config['rows']
        columns = config['columns']
        all_frames = config['all_frames']
        frames = []
        for i in range(rows):
            for j in range(columns):
                frames.append(sprite_sheet.subsurface(
                    (size[0] * j, size[1] * i, size[0], size[1])))
                if len(frames) == all_frames:
                    break
        return frames


Images = Images_Loader()
