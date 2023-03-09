import pygame
from dino_runner.components.text import Text
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE, HEART_TYPE, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING,JUMPING,DUCKING, RUNNING_HAMMER, RUNNING_SHIELD, SCREEN_WIDTH, SHIELD_TYPE
DINO_RUNING = 'runing'
DINO_JUMPING = 'jumping'
DINO_DUCK = 'duck'

DUCK_IMG = {DEFAULT_TYPE: DUCKING, HEART_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER }
JUMP_IMG = {DEFAULT_TYPE: JUMPING, HEART_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, HEART_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
class Dinosaur(pygame.sprite.Sprite):
    P_x = 80
    P_y = 310
    j_velocity = 8.5
    def __init__(self):
        self.half_screen_width = SCREEN_WIDTH // 2
        self.tipe = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.update_image(RUN_IMG[self.tipe][0])
        self.rect = self.image.get_rect()
        self.rect.x = self.P_x
        self.rect.y = self.P_y
        self.step = 0
        self.action = DINO_RUNING
        self.jump_velocity = self.j_velocity

        self.text = Text()

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
        self.update_image(RUN_IMG[self.tipe][self.step//5])
        self.step += 1

    def jump(self):
        pos_y=self.rect.y - self.jump_velocity * 4
        self.update_image(JUMP_IMG[self.tipe],pos_y=pos_y)
        self.jump_velocity -= 0.8
        print("VELOCITY ::", self.jump_velocity)
        if self.jump_velocity <= -self.j_velocity:
            self.jump_velocity = self.j_velocity
            self.action = DINO_RUNING
            self.rect.y = self.P_y

    def duck(self):
        self.update_image(DUCK_IMG[self.tipe][self.step//5],pos_y=340)
        self.step += 1

    def update_image(self,image: pygame.Surface, pos_x = None,pos_y = None):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos_x or self.P_x
        self.rect.y = pos_y or self.P_y

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.tipe = power_up.type
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000)

    def check_power_up(self, screen):
        if self.tipe == SHIELD_TYPE or self.tipe == HAMMER_TYPE or self.tipe == HEART_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.text.show(self.half_screen_width,50,f"{self.tipe.capitalize()} enabled for {time_to_show} seconds.",18,screen)
            else:
                self.tipe = DEFAULT_TYPE
                self.power_up_time_up = 0
