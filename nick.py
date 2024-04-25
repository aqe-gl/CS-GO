import arcade
import animate
from constants import *


class Nick(animate.Animate):
    def __init__(self):
        super().__init__('go_bill/0.gif', SCALING)
        self.center_x = 100
        self.center_y = 100
        self.left_textures = []
        self.right_textures = []
        self.side = 'right'
        self.right_down = arcade.load_texture('bill_textures/BillLayingDown.png', flipped_horizontally=False)
        self.left_down = arcade.load_texture('bill_textures/BillLayingDown.png', flipped_horizontally=True)
        for i in range(6):
            self.left_textures.append(arcade.load_texture(f'go_bill/{i}.gif', flipped_horizontally=True))
            self.right_textures.append(arcade.load_texture(f'go_bill/{i}.gif', flipped_horizontally=False))

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def set_side(self):
        if self.side == 'left':
            self.textures = self.left_textures
        elif self.side == 'right':
            self.textures = self.right_textures

    def to_down(self):
        if self.side == 'right':
            self.texture = self.right_down
        elif self.side == 'left':
            self.texture = self.left_down

    def next_slide(self):
        if self.left >= SCREEN_WIDTH:
            self.center_x = 0
            return True
        return False

    def previous_slide(self):
        if self.right <= 0:
            self.center_x = SCREEN_WIDTH
            return True
        return False
