from dino_runner.components.obstacles.cactus import CactusB, CactusS
from dino_runner.components.obstacles.bird import Bird
import pygame
import random
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self,game_speed,player,game):
        if not self.obstacles:
            ob = random.randint(0,2)
            if ob == 0:
                self.obstacles.append(CactusB())
            elif ob == 1:
                self.obstacles.append(CactusS())
            elif ob == 2:
                self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)