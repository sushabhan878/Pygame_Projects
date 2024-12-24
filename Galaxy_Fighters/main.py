import pygame
import os

# Initialize pygame modules
pygame.font.init()  # Initialize font module
pygame.mixer.init()  # Initialize sound module

# Set display dimensions and initialize the game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fighters")

# Define colors using RGB tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Define the middle border separating the two players
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

# Game constants
FPS = 60  # Frames per second
VELO = 5  # Velocity of spaceship movement
BULLET_VELO = 7  # Velocity of bullets
MAX_BUL = 11111  # Maximum bullets allowed on screen
SPACESHIP_WIDTH = 55  # Width of each spaceship
SPACESHIP_HEIGHT = 40  # Height of each spaceship

# Custom Pygame events for bullet hits
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Load assets
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90
)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270
)

# Initialize fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Load sound effects
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

def draw_window(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health):
    """
    Draws all elements on the game window.
    Args:
        red, yellow: Rect objects for the red and yellow spaceships
        yellow_bullets, red_bullets: Lists of Rect objects representing bullets
        yellow_health, red_health: Integer health values for each player
    """
    WIN.blit(SPACE, (0, 0))  # Draw the background
    pygame.draw.rect(WIN, BLACK, BORDER)  # Draw the border

    # Draw health text
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))

    # Draw spaceships
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    # Draw bullets
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()  # Refresh the display

def yellow_handle_movement(keys_pressed, yellow):
    """Handles movement for the yellow spaceship based on key presses."""
    if keys_pressed[pygame.K_a] and yellow.x - VELO >= 0:  # Move left
        yellow.x -= VELO
    if keys_pressed[pygame.K_d] and yellow.x + VELO + yellow.width <= BORDER.x:  # Move right
        yellow.x += VELO
    if keys_pressed[pygame.K_w] and yellow.y - VELO >= 0:  # Move up
        yellow.y -= VELO
    if keys_pressed[pygame.K_s] and yellow.y + VELO + yellow.height <= HEIGHT - 15:  # Move down
        yellow.y += VELO

def red_handle_movement(keys_pressed, red):
    """Handles movement for the red spaceship based on key presses."""
    if keys_pressed[pygame.K_LEFT] and red.x - VELO >= BORDER.x + BORDER.width:  # Move left
        red.x -= VELO
    if keys_pressed[pygame.K_RIGHT] and red.x + VELO + red.width <= WIDTH + 15:  # Move right
        red.x += VELO
    if keys_pressed[pygame.K_UP] and red.y - VELO >= 0:  # Move up
        red.y -= VELO
    if keys_pressed[pygame.K_DOWN] and red.y + VELO + red.height <= HEIGHT - 15:  # Move down
        red.y += VELO

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """Updates bullet positions and checks for collisions."""
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELO  # Move bullet right
        if red.colliderect(bullet):  # Check collision with red spaceship
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELO  # Move bullet left
        if yellow.colliderect(bullet):  # Check collision with yellow spaceship
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

def draw_winner(text):
    """Displays the winner text and pauses for a moment."""
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)  # Delay to allow players to see the result

def main():
    """Main function to run the game loop."""
    # Initialize player rectangles
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Initialize bullets and health
    yellow_bullets = []
    red_bullets = []
    yellow_health = 10
    red_health = 10

    run = True
    clock = pygame.time.Clock()  # Create a clock to manage FPS

    while run:
        clock.tick(FPS)  # Control the game's frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle quit event
                run = False

            # Handle shooting bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BUL:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height / 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BUL:
                    bullet = pygame.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # Handle bullet hits
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

        # Check for winner
        winner_text = ""
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        # Handle player movement
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        # Update game elements
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health)

    pygame.quit()  # Quit the game

if __name__ == "__main__":
    main()
