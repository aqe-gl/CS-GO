import arcade
from constants import *


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()
        self.background_textures = []
        for i in range(1, 16):
            self.background_textures.append(arcade.load_texture(f'background/Map{i}.png'))
        self.index_texture = 0

    def setup(self):
        pass

    def update(self, delta_time: float):
        pass

    def on_draw(self):
        self.clear((255, 255, 255))

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
