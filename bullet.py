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
        if abs(self.center_x - self.game.nick.center_x) > BULLET_DISTANCE:
            self.kill()

        snipers = arcade.check_for_collision_with_list(self, self.game.snipers)
        for i in snipers:
            i.lives -= 1
            arcade.play_sound(self.game.coin_sound)

        runmen = arcade.check_for_collision_with_list(self, self.game.enemies)
        for runman in runmen:
            runman.lives -= 1
            arcade.play_sound(self.game.coin_sound)

        if len(snipers) > 0 or len(runmen) > 0:
            self.kill()


class SniperBullet(Bullet):
    def __init__(self, window, direction_x, direction_y, x, y):
        super().__init__(window)
        self.set_position(x, y + 10)
        self.change_x = direction_x
        self.change_y = direction_y
        self.created_x = x

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if abs(self.center_x - self.created_x) > BULLET_DISTANCE:
            self.kill()
        if arcade.check_for_collision(self, self.game.nick):
            self.game.nick.lives -= 1
            arcade.play_sound(self.game.nick.pain_sound)
            self.kill()

