import pygame
from dino_runner.utils.constants import FONT_TIPE

class Score:
    def __init__(self,score):
        self.score = score

    def update(self,game,playing):
        if playing==True:
            self.score += 1
        elif playing == False:
            self.score -= 0
        if self.score % 100 == 0:
            game.game_speed += 2

        return self.score

    def draw(self,screen):
        font = pygame.font.Font(FONT_TIPE, 32)
        text = font.render(f"score:{self.score}",True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (950, 30)
        screen.blit(text, text_rect)