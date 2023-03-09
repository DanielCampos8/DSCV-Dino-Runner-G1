import random

import pygame
from dino_runner.components.power_ups.hamer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield


class PowerUpManager:
    def __init__(self):
        self.power_ups: list[PowerUp] = []
        self.when_appears = 0

    def update(self,game_speed,score,player):
        if not self.power_ups and score == self.when_appears:
            self.when_appears += random.randint(100,300)
            p_up = random.randint(0,2)
            if p_up == 0:
                self.power_ups.append(Shield())
            elif p_up == 1:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Heart())

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if power_up.rect.colliderect(player.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up)
                self.power_ups.remove(power_up)


    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 300)