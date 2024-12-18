import pygame
import time
import random
pygame.font.init()

# Constants
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("./asset/space.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELO = 5
FONT = pygame.font.SysFont("comicsans", 30)
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELO = 10

# Function to draw everything
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))  # Draw background
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    pygame.draw.rect(WIN, "red", player)  # Draw player rectangle
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    pygame.display.update()  # Update the screen

def main():
    run = True

    # Initialize player rectangle
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()  # Add clock for FPS control

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)  # Cap the game loop to 60 FPS
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, - STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # Movement handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELO >= 0:  # Prevent going out of bounds
            player.x -= PLAYER_VELO
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELO + PLAYER_WIDTH <= WIDTH:  # Prevent going out of bounds
            player.x += PLAYER_VELO

        for star in stars[:]:
            star.y += STAR_VELO
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            break
        
        # Draw the updated frame
        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()
