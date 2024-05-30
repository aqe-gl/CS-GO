import arcade
import time
import bullet


class Sniper(arcade.Sprite):
    def __init__(self, window):
        super().__init__('sniper/sniper_forward.png', 1)
        self.game = window

        self.lives = 1
        self.sniper_left = arcade.load_texture('sniper/sniper_forward.png')
        self.sniper_right = arcade.load_texture('sniper/sniper_forward.png', flipped_horizontally=True)
        self.sniper_left_angle = arcade.load_texture('sniper/sniper_angle.png')
        self.sniper_right_angle = arcade.load_texture('sniper/sniper_angle.png', flipped_horizontally=True)
        self.last_reloading = time.time()

    def update(self):
        if self.game.nick.center_y < self.center_y:
            if self.game.nick.center_x < self.center_x:
                self.texture = self.sniper_left_angle
                self.shot(-10, -10)
            else:
                self.texture = self.sniper_right_angle
                self.shot(10, -10)
        else:
            if self.game.nick.center_x < self.center_x:
                self.texture = self.sniper_left
                self.shot(-10, 0)
            else:
                self.texture = self.sniper_right
                self.shot(10, 0)

    def shot(self, direction_x, direction_y):
        if time.time() - self.last_reloading > 3:
            x = self.center_x
            y = self.center_y
            new_bullet = bullet.SniperBullet(self.game, direction_x, direction_y, x, y)
            self.game.sniper_bullets.append(new_bullet)
            self.last_reloading = time.time()