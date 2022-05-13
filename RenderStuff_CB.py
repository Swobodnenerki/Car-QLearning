import pyglet
from pyglet.gl import *
import pygame
import math
from pyglet.window import key
from Drawer import Drawer
# from PygameAdditionalMethods import *
from ShapeObjects import Line
import tensorflow as tf  # Deep Learning library
import numpy as np  # Handle matrices
from collections import deque
import random
import os
from Globals import displayHeight, displayWidth
from Game import Game

frameRate = 7.0

vec2 = pygame.math.Vector2

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        # load background image
        self.game = Game()

    def on_draw(self):
        self.game.render()


if __name__ == "__main__":
    window = MyWindow(displayWidth, displayHeight, "AI Learns to Drive", resizable=False)
    #pyglet.clock.schedule_interval(window.update, 1 / frameRate)
    pyglet.app.run()
