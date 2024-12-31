import pygame
import os
import time 
import random
pygame.font.init()


WIDTH, HEIGHT = 850, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

RED_SPACE_player = pygame.image.load(os.path.join("Assets", "pixel_ship_red_small.png"))
GREEN_SPACE_player = pygame.image.load(os.path.join("Assets", "pixel_ship_green_small.png"))
BLUE_SPACE_player = pygame.image.load(os.path.join("Assets", "pixel_ship_blue_small.png"))


YELLOW_SPACE_player = pygame.image.load(os.path.join("Assets", "pixel_ship_yellow.png"))


RED_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_yellow.png"))


BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background-black.png")), (WIDTH, HEIGHT))


class player:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0 

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))

class Player(player):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.player_img = YELLOW_SPACE_player
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 30)
    player_velo = 5
    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        lives_lable = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_lable = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_lable, (10, 10))
        WIN.blit(level_lable, (WIDTH - level_lable.get_width() - 10, 10))

        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_velo > 0:
            player.x -= player_velo
        if keys[pygame.K_d] and player.x + player_velo + 50 < WIDTH:
            player.x += player_velo
        if keys[pygame.K_w] and player.y - player_velo > 0:
            player.y -= player_velo
        if keys[pygame.K_s] and player.y + player_velo + 50 < HEIGHT:
            player.y += player_velo
main()