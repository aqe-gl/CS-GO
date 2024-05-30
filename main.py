import arcade

import line
from constants import *
from nick import *
from line import *
from bullet import *
from run_man import *
import random
from sniper import *
from coords import *


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
        self.down_pressed = False
        self.lines_for_level = []
        self.run_men_for_level = []
        self.run_men_engine = []
        self.snipers_for_level = []
        # Sprites
        self.nick = Nick()
        # Sprite Lists
        self.lines = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.snipers = arcade.SpriteList()
        self.sniper_bullets = arcade.SpriteList()
        self.shoot_sound = arcade.Sound('sounds/shoot.wav')
        self.jump_sound = arcade.Sound('sounds/jump.wav')

        # Music
        # self.music = arcade.Sound('sounds/Metallica Master Of Puppets.mp3')

        self.setup()

        # Physics
        self.engine = arcade.PhysicsEnginePlatformer(self.nick, self.lines, GRAVITY)

        # self.music.play(1)

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
            self.run_men_for_level.append([])
            for x, y in lines:
                other_line = line.Line()
                other_line.set_position(x, y)
                self.lines_for_level[i].append(other_line)
                # Run men
                new_run_man = Runman(self)
                if x == -100:
                    new_run_man.set_position(random.randint(50, SCREEN_WIDTH - 50), 100)
                else:
                    new_run_man.set_position(x, y + 50)

                self.run_men_for_level[i].append(new_run_man)

        for i, snipers in enumerate(COORDS_SNIPERS):
            self.snipers_for_level.append([])
            for x, y in snipers:
                new_sniper = Sniper(self)
                new_sniper.set_position(x, y)
                self.snipers_for_level[i].append(new_sniper)

        self.append_line(0)

    def update(self, delta_time: float):
        if self.game:
            self.nick.update()
            self.engine.update()
            self.bullets.update()
            self.enemies.update_animation(delta_time)
            self.enemies.update()
            self.snipers.update()
            self.sniper_bullets.update()

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
            for i in self.run_men_engine:
                i.update()

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background_textures[self.index_texture])
        self.nick.draw()
        self.lines.draw()
        self.bullets.draw()
        self.enemies.draw()
        self.snipers.draw()
        self.sniper_bullets.draw()

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
            self.down_pressed = True

        if symbol == arcade.key.UP:
            if self.engine.can_jump():
                self.engine.jump(JUMP)
                self.jump_sound.play(1)

        if symbol == arcade.key.SPACE:
            new_bullet = Bullet(self)
            new_bullet.set_position(self.nick.center_x + 10, self.nick.center_y + 10)
            self.shoot_sound.play(1)
            if self.down_pressed:
                new_bullet.center_y = self.nick.center_y - 15
            self.bullets.append(new_bullet)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT or symbol == arcade.key.DOWN:
            self.nick.change_x = 0
            self.is_walk = False
            self.nick.set_texture(0)
            self.down_pressed = False

    def append_line(self, side):
        self.append_run_man(side)
        self.append_sniper(side)
        if side:
            for i in range(len(self.lines_for_level[self.index_texture + side])):
                self.lines.pop()
        for new_line in self.lines_for_level[self.index_texture]:
            self.lines.append(new_line)

    def append_run_man(self, side):
        self.run_men_engine.clear()
        if side:
            for i in range(len(self.run_men_for_level[self.index_texture + side])):
                self.enemies.pop()
        for new_run_man in self.run_men_for_level[self.index_texture]:
            self.enemies.append(new_run_man)
            self.run_men_engine.append(arcade.PhysicsEnginePlatformer(new_run_man, self.lines, GRAVITY))


    def append_sniper(self, side):
        if side:
            for i in range(len(self.snipers_for_level[self.index_texture + side])):
                self.snipers.pop()
        for new_sniper in self.snipers_for_level[self.index_texture]:
            self.snipers.append(new_sniper)



game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
