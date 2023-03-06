import pygame
from dino_runner.utils.constants import RUNNING,JUMPING,DUCKING
DINO_RUNING = 'runing'
DINO_JUMPING = 'jumping'
DINO_DUCK = 'duck'
class Dinosaur(pygame.sprite.Sprite):
    P_x = 80
    P_y = 310
    j_velocity = 8.5
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.P_x
        self.rect.y = self.P_y
        self.step = 0
        self.action = DINO_RUNING
        self.jump_velocity = self.j_velocity

    def update(self,user_imput):
        if self.action == DINO_RUNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCK:
            self.duck()
        
        #actions
        if user_imput[pygame.K_UP]:
            self.action = DINO_JUMPING
        elif user_imput[pygame.K_DOWN]:
            self.action = DINO_DUCK
        elif self.action != DINO_JUMPING or self.action != DINO_DUCK:
            self.action = DINO_RUNING

        if self.step >= 10:
            self.step = 0

    def run(self):
        self.image = RUNNING[self.step//5]
        self.rect = self.image.get_rect()
        self.rect.x = self.P_x
        self.rect.y = self.P_y
        self.step += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        print("VELOCITY ::", self.jump_velocity)
        if self.jump_velocity <= -self.j_velocity:
            self.jump_velocity = self.j_velocity
            self.action = DINO_RUNING
            self.rect.y = self.P_y

    def duck(self):
        self.new_y = 340
        self.image = DUCKING[self.step//5]
        self.rect = self.image.get_rect()
        self.rect.x = self.P_x
        self.rect.y = self.new_y
        self.step += 1

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

dinosaur = Dinosaur()