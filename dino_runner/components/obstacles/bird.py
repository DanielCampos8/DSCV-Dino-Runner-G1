from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import pygame
import random

class Bird(Obstacle):
    def __init__(self):
        self.step = 0
        self.image = BIRD[self.step//5]
        super().__init__(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(220, 350)
        self.step += 1

        if self.step >= 10:
            self.step = 0