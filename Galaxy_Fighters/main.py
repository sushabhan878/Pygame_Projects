import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galexy Fighters")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VELO = 5
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), (90))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), (270))

def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELO >= 0:       # Yellow Left 
        yellow.x -= VELO
    if keys_pressed[pygame.K_d] and yellow.x + VELO + yellow.width <= BORDER.x:       # Yellow Right
        yellow.x += VELO
    if keys_pressed[pygame.K_w] and yellow.y - VELO >= 0:       # Yellow Top
        yellow.y -= VELO
    if keys_pressed[pygame.K_s] and yellow.y + VELO + yellow.height <= HEIGHT - 15:       # Yellow Bottom
        yellow.y += VELO  

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELO >= BORDER.x + BORDER.width:       # Red Left 
        red.x -= VELO
    if keys_pressed[pygame.K_RIGHT] and red.x + VELO + red.width <= WIDTH + 15:       # Red Right
        red.x += VELO
    if keys_pressed[pygame.K_UP] and red.y - VELO >= 0:       # Red Top
        red.y -= VELO
    if keys_pressed[pygame.K_DOWN] and red.y + VELO + red.height <= HEIGHT - 15:       # Red Bottom
        red.y += VELO  

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()  
     
if __name__ =="__main__":
    main()
