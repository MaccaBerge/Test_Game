



class Settings:
    def __init__(self) -> None:
        self.screen_size = (1200, 800)
        self.display_size = (self.screen_size[0] / 2, self.screen_size[1] / 2)

        self.target_fps = 60

        self.asset_paths = {
            "animation" : "Assets/Animation"
        }
