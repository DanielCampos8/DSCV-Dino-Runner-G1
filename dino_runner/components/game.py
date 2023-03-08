import pygame
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.components.text import Text

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS, FONT_TIPE, DINO_START
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0

        self.player = Dinosaur()
        self.manager = ObstacleManager()
        self.score = Score()
        self.text = Text()
        self.power_ups_manager = PowerUpManager()

    def run(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def start_game(self):
        # Game loop: events - update - draw
        self.game_speed = 20
        self.playing = True
        self.score.reset()
        self.manager.reset()
        self.power_ups_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_imput = pygame.key.get_pressed()
        self.player.update(user_imput)
        self.manager.update(self.game_speed,self.player,self.on_death)
        self.score.update(self,self.playing)
        self.score.update_max_score()
        self.power_ups_manager.update(self.game_speed, self.score.score, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.manager.draw(self.screen)
        self.player.draw(self.screen)
        self.score.draw(self.screen)
        self.power_ups_manager.draw(self.screen)
        self.player.check_power_up(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        is_invincible = self.player.tipe == SHIELD_TYPE
        if not is_invincible:
            self.playing = False
            self.death_count +=1

    def show_menu(self):
        #pantalla en blanco 
        self.screen.fill((255,255,255))
        #mensaje de bienvenida centrado
        self.half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            self.text.show(self.half_screen_width, half_screen_height,"Welcome, press any key to start!",32,self.screen)
        else:
            attemp =f"death:{self.death_count}"
            score =f"score:{self.score.update(self, self.playing)}"
            death_text_y = half_screen_height + 40
            score_text_y = half_screen_height + 65
            restart_text_y = half_screen_height + 80
            x=self.half_screen_width

            #mostrar mensaje para que reinicie,cuantas veces muere
            self.text.show(x,half_screen_height,"game over",32,self.screen)
            self.text.show(x,death_text_y,attemp,20,self.screen)
            self.text.show(x,score_text_y,score,20,self.screen)
            self.text.show(x,restart_text_y,"press any key to restart",15,self.screen)
            pass
            #icono al centro
        self.screen.blit(DINO_START,(self.half_screen_width -
                                    40, half_screen_height - 140))

        #plasmar cambios
        pygame.display.update()
        #manejar los eventos
        self.handle_menu_events()


    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            
            elif event.type == pygame.KEYDOWN:
                self.start_game()