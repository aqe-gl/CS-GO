import arcade
from constants import *
from nick import *


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()
        self.background_textures = []
        for i in range(1, 16):
            self.background_textures.append(arcade.load_texture(f'background/Map{i}.png'))
        self.index_texture = 0
        self.game = True
        self.nick = Nick()
        self.is_walk = False
        self.lines = arcade.SpriteList()


    def setup(self):
        pass

    def update(self, delta_time: float):
        if self.game:
            self.nick.update()
            if self.is_walk:
                self.nick.update_animation(delta_time)

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_textures[self.index_texture])
        self.nick.draw()
        self.lines.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.is_walk = True
            self.nick.side = 'left'
            self.nick.set_side()
            self.nick.change_x = -PLAYER_MOVEMENT_SPEED

        if symbol == arcade.key.RIGHT:
            self.is_walk = True
            self.nick.side = 'right'
            self.nick.set_side()
            self.nick.change_x = PLAYER_MOVEMENT_SPEED

        if symbol == arcade.key.DOWN:
            self.nick.to_down()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT or symbol == arcade.key.DOWN:
            self.nick.change_x = 0
            self.is_walk = False
            self.nick.set_texture(0)


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
