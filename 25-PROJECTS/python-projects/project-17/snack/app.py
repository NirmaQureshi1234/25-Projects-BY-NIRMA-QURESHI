import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)  # For difficulty level text

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Font for displaying score and messages
font = pygame.font.SysFont("Arial", 25)

# Function to display the score
def display_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Function to display the high score
def display_high_score(high_score):
    text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH - 200, 10))

# Function to draw the snake
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Function to generate food
def generate_food():
    food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return (food_x, food_y)

# Function to display a message box
def display_message(message, y_offset=0):
    text = font.render(message, True, WHITE, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)

# Function to reset the game
def reset_game():
    snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    direction = "RIGHT"
    food = generate_food()
    score = 0
    return snake, direction, food, score

# Main game loop
def main():
    snake, direction, food, score = reset_game()
    high_score = 0
    game_over = False
    difficulty = 5  # Initial game speed (FPS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

                # Restart game on pressing 'R'
                if event.key == pygame.K_r and game_over:
                    snake, direction, food, score = reset_game()
                    game_over = False

                # Quit game on pressing 'Q'
                if event.key == pygame.K_q and game_over:
                    pygame.quit()
                    return

                # Adjust difficulty (speed) on pressing '1', '2', or '3'
                if event.key == pygame.K_1:
                    difficulty = 5  # Slow speed
                if event.key == pygame.K_2:
                    difficulty = 10  # Medium speed
                if event.key == pygame.K_3:
                    difficulty = 15  # Fast speed

        if not game_over:
            # Move the snake
            head_x, head_y = snake[0]
            if direction == "UP":
                new_head = (head_x, head_y - BLOCK_SIZE)
            if direction == "DOWN":
                new_head = (head_x, head_y + BLOCK_SIZE)
            if direction == "LEFT":
                new_head = (head_x - BLOCK_SIZE, head_y)
            if direction == "RIGHT":
                new_head = (head_x + BLOCK_SIZE, head_y)

            # Check for collisions
            if (
                new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
                new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
                new_head in snake
            ):
                game_over = True
                if score > high_score:
                    high_score = score

            # Add new head to the snake
            snake.insert(0, new_head)

            # Check if snake eats food
            if new_head == food:
                food = generate_food()
                score += 1
            else:
                snake.pop()

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
        display_score(score)
        display_high_score(high_score)

        # Display difficulty level
        difficulty_text = font.render(f"Speed: {difficulty} (Press 1, 2, 3 to change)", True, BLUE)
        screen.blit(difficulty_text, (10, SCREEN_HEIGHT - 40))

        if game_over:
            display_message(f"Game Over! Score: {score}", y_offset=-50)
            display_message("Press R to Restart or Q to Quit", y_offset=50)

        pygame.display.flip()
        clock.tick(difficulty)  # Control game speed based on difficulty

if __name__ == "__main__":
    main()