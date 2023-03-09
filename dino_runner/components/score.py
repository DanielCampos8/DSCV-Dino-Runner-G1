import pygame
from dino_runner.utils.constants import HAMMER_TYPE, HEART_TYPE
from dino_runner.components.text import Text

class Score:
    def __init__(self):
        self.score = 0
        self.max_score = 0
        self.text = Text()

    def update(self,game,playing,power_up):
        self.tipe = power_up
        if playing:
            self.score += 1
        elif not playing:
            self.score -= 0
        #si tiene el martillo baja la velocidad del juego    
        if self.tipe == HEART_TYPE:
            game.game_speed = 20
        elif self.score % 100 == 0:
            game.game_speed += 2
        #si agarra el corazon acelera el juego
        if self.tipe == HAMMER_TYPE and self.score % 20 == 0:
            game.game_speed += 2
        elif self.score % 100 == 0:
            game.game_speed += 2
         

        return self.score

    def update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score

    def reset(self):
        self.score = 0

    def draw(self,screen):
        self.text.show(850,30,f"score:{self.score}",32,screen)
        self.text.show(1000,30,f"hi:{self.max_score}",32,screen)
        