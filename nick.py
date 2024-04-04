import arcade
import animate
from constants import *


class Nick(animate.Animate):
    def __init__(self):
        super().__init__('go_bill/0.gif', SCALING)
        self.center_x = 100
        self.center_y = 100
        for i in range(6):
            self.append_texture(arcade.load_texture(f'go_bill/{i}.gif'))
