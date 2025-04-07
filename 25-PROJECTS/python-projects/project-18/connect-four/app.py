import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
DISC_SIZE = 100
GRID_WIDTH = 7
GRID_HEIGHT = 6

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)  # Grid background color

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect Four")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Font for displaying messages
font = pygame.font.SysFont("Arial", 50)

# Initialize grid
grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Function to draw the grid
def draw_grid():
    # Draw grid background
    pygame.draw.rect(screen, BLUE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Draw grid cells
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.circle(screen, WHITE, (x * DISC_SIZE + DISC_SIZE // 2, y * DISC_SIZE + DISC_SIZE // 2), DISC_SIZE // 2 - 5)

# Function to draw the discs
def draw_discs():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == "R":
                pygame.draw.circle(screen, RED, (x * DISC_SIZE + DISC_SIZE // 2, y * DISC_SIZE + DISC_SIZE // 2), DISC_SIZE // 2 - 5)
            elif grid[y][x] == "Y":
                pygame.draw.circle(screen, YELLOW, (x * DISC_SIZE + DISC_SIZE // 2, y * DISC_SIZE + DISC_SIZE // 2), DISC_SIZE // 2 - 5)

# Function to drop a disc
def drop_disc(column, player):
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if grid[y][column] is None:
            grid[y][column] = player
            return True
    return False

# Function to check for a win
def check_win(player):
    # Check horizontal
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH - 3):
            if grid[y][x] == grid[y][x + 1] == grid[y][x + 2] == grid[y][x + 3] == player:
                return True

    # Check vertical
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT - 3):
            if grid[y][x] == grid[y + 1][x] == grid[y + 2][x] == grid[y + 3][x] == player:
                return True

    # Check diagonal (top-left to bottom-right)
    for y in range(GRID_HEIGHT - 3):
        for x in range(GRID_WIDTH - 3):
            if grid[y][x] == grid[y + 1][x + 1] == grid[y + 2][x + 2] == grid[y + 3][x + 3] == player:
                return True

    # Check diagonal (bottom-left to top-right)
    for y in range(3, GRID_HEIGHT):
        for x in range(GRID_WIDTH - 3):
            if grid[y][x] == grid[y - 1][x + 1] == grid[y - 2][x + 2] == grid[y - 3][x + 3] == player:
                return True

    return False

# Function to reset the game
def reset_game():
    global grid, current_player, game_over
    grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    current_player = "R"
    game_over = False

# Function to display a message box
def display_message(message, y_offset=0):
    text = font.render(message, True, WHITE, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)

# Main game loop
def main():
    global current_player, game_over
    current_player = "R"
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, _ = event.pos
                column = x // DISC_SIZE
                if drop_disc(column, current_player):
                    if check_win(current_player):
                        game_over = True
                    current_player = "Y" if current_player == "R" else "R"

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:  # Restart game
                    reset_game()
                if event.key == pygame.K_q:  # Quit game
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        draw_grid()
        draw_discs()

        if game_over:
            display_message(f"Player {current_player} wins!", y_offset=-50)
            display_message("Press R to Restart or Q to Quit", y_offset=50)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()