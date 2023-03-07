from dino_runner.components.obstacles.smallcactus import SmallCactus
from dino_runner.components.obstacles.largecactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
import pygame
import random
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self,game_speed,player,on_death):
        if not self.obstacles:
            ob = random.randint(0,2)
            if ob == 0:
                self.obstacles.append(LargeCactus())
            elif ob == 1:
                self.obstacles.append(SmallCactus())
            else:
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                on_death()

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []