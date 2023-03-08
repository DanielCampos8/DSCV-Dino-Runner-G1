import pygame
from dino_runner.utils.constants import FONT_TIPE
from dino_runner.components.text import Text

class Score:
    def __init__(self):
        self.score = 0
        self.max_score = 0
        self.text = Text()

    def update(self,game,playing):
        if playing:
            self.score += 1
        elif not playing:
            self.score -= 0
        if self.score % 100 == 0:
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
        