import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader (Winning Condition)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Player settings
player_width = 50
player_height = 10
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 5

# Enemy settings
enemy_radius = 20
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = 50
enemy_speed = 3
enemy_direction = 1  # 1 = right, -1 = left

# Bullet settings
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Game variables
score = 0
lives = 3
WINNING_SCORE = 10  # Change this to set how many points to win
running = True

# Function to check collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    return distance < enemy_radius  # If distance is smaller than radius, it's a hit!

# Game loop
while running:
    screen.fill(BLACK)  # Clear screen
    pygame.time.delay(20)  # Frame rate control

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Shoot immediately
                bullets.append([player_x + player_width // 2, player_y])

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Enemy movement
    enemy_x += enemy_speed * enemy_direction
    if enemy_x <= 0 or enemy_x >= WIDTH - enemy_radius:
        enemy_direction *= -1  # Change direction

    # Bullet movement
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)  # Remove bullet if it goes off-screen

    # Collision detection (bullet hits enemy)
    for bullet in bullets[:]:
        if is_collision(enemy_x, enemy_y, bullet[0], bullet[1]):
            bullets.remove(bullet)
            score += 1  # Increase score
            enemy_x = random.randint(50, WIDTH - 50)  # Respawn enemy
            enemy_y = 50  # Reset enemy position at the top

    # Enemy reaching bottom (Lose a life)
    if enemy_y >= HEIGHT - 50:
        lives -= 1
        enemy_y = 50
        enemy_x = random.randint(50, WIDTH - 50)  # Respawn enemy

    # **Winning Condition**
    if score >= WINNING_SCORE:
        screen.fill(BLACK)
        win_text = font.render("You Win! Press Q to Quit", True, YELLOW)
        screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.update()

        # Wait for player to quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    waiting = False
                    running = False

    # **Game Over Condition**
    if lives <= 0:
        screen.fill(BLACK)
        game_over_text = font.render("Game Over! Press Q to Quit", True, YELLOW)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.update()

        # Wait for player to quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    waiting = False
                    running = False

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw enemy
    pygame.draw.circle(screen, RED, (enemy_x, enemy_y), enemy_radius)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Display Score and Lives
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    pygame.display.update()  # Update screen

pygame.quit()
