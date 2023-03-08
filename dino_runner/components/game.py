import pygame
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_TIPE, DINO_START
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

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.manager.draw(self.screen)
        self.player.draw(self.screen)
        self.score.draw(self.screen)
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
        self.playing = False
        self.death_count +=1

    def show_menu(self):
        #pantalla en blanco 
        self.screen.fill((255,255,255))
        #mensaje de bienvenida centrado
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            self.text(half_screen_width, half_screen_height,"Welcome, press any key to start!",32)
        else:
            death_text = half_screen_height + 40
            score_text = half_screen_height + 65
            restart_text = half_screen_height + 80
            attemp =f"death:{self.death_count}"
            score =f"score:{self.score.update(self, self.playing)}"
            #mostrar mensaje para que reinicie,cuantas veces muere
            self.text(half_screen_width, half_screen_height,"you lose",32)
            self.text(half_screen_width, death_text,attemp,20)
            self.text(half_screen_width, score_text,score,20)
            self.text(half_screen_width, restart_text,"press any key to restart",15)
            pass
            #icono al centro
        self.screen.blit(DINO_START,(half_screen_width -
                                    40, half_screen_height - 140))

        #plasmar cambios
        pygame.display.update()
        #manejar los eventos
        self.handle_menu_events()

    def text(self,x,y,text,size):
        font = pygame.font.Font(FONT_TIPE, size)
        text = font.render(text,True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            
            elif event.type == pygame.KEYDOWN:
                self.start_game()