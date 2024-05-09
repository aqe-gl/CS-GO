import arcade
import animate
from constants import SCALING


class Runman(animate.Animate):
    def __init__(self):
        super().__init__('runman/frame-01.gif', SCALING)
        self.lives = 3
        self.left_textures = []
        self.right_textures = []
        for i in range(1, 10):
            self.left_textures.append(arcade.load_texture(f'runman/frame-0{i}.gif', flipped_horizontally=False))
            self.right_textures.append(arcade.load_texture(f'runman/frame-0{i}.gif', flipped_horizontally=True))
        self.side = False