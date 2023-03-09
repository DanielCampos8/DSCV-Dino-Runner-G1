import pygame
from dino_runner.utils.constants import FONT_TIPE

class Text:
    def show(self,x,y,text,size,screen):
            font = pygame.font.Font(FONT_TIPE, size)
            text = font.render(text,True,(0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (x, y)
            screen.blit(text, text_rect)