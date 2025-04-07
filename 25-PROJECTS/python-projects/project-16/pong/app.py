import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Ball dimensions
BALL_SIZE = 20

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Font for displaying score and messages
font = pygame.font.SysFont("Arial", 50)

# Function to draw the paddles
def draw_paddles(paddle1, paddle2):
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)

# Function to draw the ball
def draw_ball(ball):
    pygame.draw.ellipse(screen, WHITE, ball)

# Function to draw the center line
def draw_center_line():
    for y in range(0, SCREEN_HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 2, y, 4, 10))

# Function to display the score
def display_score(score1, score2):
    text1 = font.render(str(score1), True, WHITE)
    text2 = font.render(str(score2), True, WHITE)
    screen.blit(text1, (SCREEN_WIDTH // 4, 20))
    screen.blit(text2, (3 * SCREEN_WIDTH // 4, 20))

# Function to display a message
def display_message(message, y_offset=0):
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)

# Function to reset the ball
def reset_ball():
    return pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Function to move the AI paddle
def move_ai_paddle(paddle, ball):
    if paddle.centery < ball.centery:
        paddle.y += 4
    elif paddle.centery > ball.centery:
        paddle.y -= 4

# Main game loop
def main():
    # Initialize paddles
    paddle1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Initialize ball
    ball = reset_ball()
    ball_speed_x = 5 * random.choice((1, -1))
    ball_speed_y = 5 * random.choice((1, -1))

    # Initialize scores
    score1 = 0
    score2 = 0

    # Game state
    game_over = False
    winner = None
    single_player = False  # Set to True for single-player mode

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:  # Restart game
                    paddle1.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
                    paddle2.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
                    ball = reset_ball()
                    score1 = 0
                    score2 = 0
                    game_over = False
                    winner = None

                if event.key == pygame.K_q and game_over:  # Quit game
                    running = False

                if event.key == pygame.K_p:  # Toggle single-player mode
                    single_player = not single_player

        if not game_over:
            # Move paddles
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and paddle1.top > 0:
                paddle1.y -= 5
            if keys[pygame.K_s] and paddle1.bottom < SCREEN_HEIGHT:
                paddle1.y += 5

            if not single_player:
                if keys[pygame.K_UP] and paddle2.top > 0:
                    paddle2.y -= 5
                if keys[pygame.K_DOWN] and paddle2.bottom < SCREEN_HEIGHT:
                    paddle2.y += 5
            else:
                move_ai_paddle(paddle2, ball)

            # Move ball
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            # Ball collision with top and bottom walls
            if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
                ball_speed_y *= -1

            # Ball collision with paddles
            if ball.colliderect(paddle1) or ball.colliderect(paddle2):
                ball_speed_x *= -1

            # Ball goes out of bounds
            if ball.left <= 0:
                score2 += 1
                ball = reset_ball()
            if ball.right >= SCREEN_WIDTH:
                score1 += 1
                ball = reset_ball()

            # Check for win condition
            if score1 >= 10:
                game_over = True
                winner = "Player 1"
            if score2 >= 10:
                game_over = True
                winner = "Player 2"

        # Draw everything
        screen.fill(BLACK)
        draw_center_line()
        draw_paddles(paddle1, paddle2)
        draw_ball(ball)
        display_score(score1, score2)

        if game_over:
            display_message(f"{winner} Wins!", y_offset=-50)
            display_message("Press R to Restart or Q to Quit", y_offset=50)

        pygame.display.flip()
        clock.tick(60)  # Control game speed (60 FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()