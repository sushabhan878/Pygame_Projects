import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galexy Fighters")

WHITE = (255, 255, 255)

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
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:       # Yellow Left 
        yellow.x -= VELO
    if keys_pressed[pygame.K_d]:       # Yellow Right
        yellow.x += VELO
    if keys_pressed[pygame.K_w]:       # Yellow Top
        yellow.y -= VELO
    if keys_pressed[pygame.K_s]:       # Yellow Bottom
        yellow.y += VELO  

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:       # Red Left 
        red.x -= VELO
    if keys_pressed[pygame.K_RIGHT]:       # Red Right
        red.x += VELO
    if keys_pressed[pygame.K_UP]:       # Red Top
        red.y -= VELO
    if keys_pressed[pygame.K_DOWN]:       # Red Bottom
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
