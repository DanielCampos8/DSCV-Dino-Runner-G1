import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image: pygame.Surface):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed,obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
