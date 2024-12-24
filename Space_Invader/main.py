import pygame
import os
import time 
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

RED_SPACE_SHIP = pygame.image.load(os.path.join("Assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("Assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("Assets", "pixel_ship_blue_small.png"))


YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Assets", "pixel_ship_yellow.png"))


RED_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Assets", "pixel_laser_yellow.png"))


BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background-black.png")), (WIDTH, HEIGHT))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
main()