import arcade


class Sniper(arcade.Sprite):
    def __init__(self):
        super().__init__('sniper/sniper_forward.png', 1)

        self.lives = 1
        self.sniper_left = arcade.load_texture('sniper/sniper_forward.png')
        self.sniper_right = arcade.load_texture('sniper/sniper_forward.png', flipped_horizontally=True)
        self.sniper_left_angle = arcade.load_texture('sniper/sniper_angle.png')
        self.sniper_right_angle = arcade.load_texture('sniper/sniper_angle.png', flipped_horizontally=True)
