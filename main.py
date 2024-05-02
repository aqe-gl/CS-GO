import arcade

import line
from constants import *
from nick import *
from line import *
from bullet import *


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Textures for background
        self.background_textures = []
        for i in range(1, 16):
            self.background_textures.append(arcade.load_texture(f'background/Map{i}.png'))
        # fields
        self.index_texture = 0
        self.game = True
        self.is_walk = False
        # Sprites
        self.nick = Nick()
        # Sprite Lists
        self.lines = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.lines_for_level = []

        self.setup()

        # Physics
        self.engine = arcade.PhysicsEnginePlatformer(self.nick, self.lines, GRAVITY)

    def setup(self):
        for i in range(0, 900, 100):
            # if i != 400:
            low_line = Line()
            low_line.set_position(i, 20)
            low_line.visible = False
            self.lines.append(low_line)
        for i, lines in enumerate(COORDS):
            print(i, lines)
            self.lines_for_level.append([])
            for x, y in lines:
                other_line = line.Line()
                other_line.set_position(x, y)
                self.lines_for_level[i].append(other_line)
        self.append_line(0)

    def update(self, delta_time: float):
        if self.game:
            self.nick.update()
            self.engine.update()
            self.bullets.update()
            if self.is_walk:
                self.nick.update_animation(delta_time)
            if self.nick.next_slide():
                if self.index_texture < len(self.background_textures) - 2:
                    self.index_texture += 1
                    self.append_line(-1)
            elif self.nick.previous_slide():
                if self.index_texture > 0:
                    self.index_texture -= 1
                    self.append_line(1)

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background_textures[self.index_texture])
        self.nick.draw()
        self.lines.draw()
        self.bullets.draw()

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

        if symbol == arcade.key.UP:
            if self.engine.can_jump():
                self.engine.jump(JUMP)

        if symbol == arcade.key.SPACE:
            new_bullet = Bullet(self)
            new_bullet.set_position(self.nick.center_x + 10, self.nick.center_y + 10)
            self.bullets.append(new_bullet)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT or symbol == arcade.key.DOWN:
            self.nick.change_x = 0
            self.is_walk = False
            self.nick.set_texture(0)

    def append_line(self, side):
        if side:
            for i in range(len(self.lines_for_level[self.index_texture + side])):
                self.lines.pop()
        for new_line in self.lines_for_level[self.index_texture]:
            self.lines.append(new_line)



game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
