import random
import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(pygame.sprite.Sprite):
    def __init__(self,image: pygame.Surface, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        self.type = type
        #tiempo en segundos de duracion del powerup
        self.duration = random.randint(5, 8)
        #en que tiempo se agarra
        self.start_time = 0

    def update(self, game_speed,power_up):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_up.remove(self)

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))