from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import pygame
import random

class Bird(Obstacle):
    def __init__(self):
        self.step = 0
        image = BIRD[0]
        super().__init__(image)
        self.rect.y = random.randint(220, 350)

    def update(self,game_speed,obstacle):
        super().update(game_speed, obstacle)
        self.image = BIRD[self.step//5]
        self.step += 1
        if self.step >= 10:
            self.step = 0