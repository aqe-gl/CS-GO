import arcade
from constants import *


class Bullet(arcade.Sprite):
    def __init__(self, game):
        super().__init__('bullet.png', 0.03)
        self.game = game
        if self.game.nick.side == 'left':
            self.change_x = -25
        else:
            self.change_x = 25


    def update(self):
        self.center_x += self.change_x
        if self.center_x - self.game.nick.center_x > BULLET_DISTANCE:
            self.kill()
