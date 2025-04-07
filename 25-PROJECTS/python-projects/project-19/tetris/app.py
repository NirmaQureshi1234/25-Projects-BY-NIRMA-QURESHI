import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan (I)
    (255, 255, 0),   # Yellow (O)
    (255, 165, 0),   # Orange (L)
    (0, 0, 255),     # Blue (J)
    (0, 255, 0),     # Green (S)
    (255, 0, 0),     # Red (Z)
    (128, 0, 128)    # Purple (T)
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 0], [1, 1, 1]]   # T
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Grid dimensions
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Initialize grid
grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Function to create a new tetromino
def create_tetromino():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return {
        "shape": shape,
        "color": color,
        "x": GRID_WIDTH // 2 - len(shape[0]) // 2,
        "y": 0
    }

# Function to draw the grid
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for y in range(GRID_HEIGHT):
        pygame.draw.line(screen, WHITE, (0, y * BLOCK_SIZE), (SCREEN_WIDTH, y * BLOCK_SIZE))
    for x in range(GRID_WIDTH):
        pygame.draw.line(screen, WHITE, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))

# Function to draw a tetromino
def draw_tetromino(tetromino):
    shape = tetromino["shape"]
    color = tetromino["color"]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, ((tetromino["x"] + x) * BLOCK_SIZE, (tetromino["y"] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

# Function to check if a tetromino is valid
def is_valid(tetromino, grid):
    shape = tetromino["shape"]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = tetromino["x"] + x
                new_y = tetromino["y"] + y
                if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or (new_y >= 0 and grid[new_y][new_x] != BLACK):
                    return False
    return True

# Function to merge tetromino into the grid
def merge_tetromino(tetromino, grid):
    shape = tetromino["shape"]
    color = tetromino["color"]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[tetromino["y"] + y][tetromino["x"] + x] = color

# Function to clear completed lines
def clear_lines(grid):
    lines_cleared = 0
    for y in range(GRID_HEIGHT):
        if all(cell != BLACK for cell in grid[y]):
            del grid[y]
            grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
            lines_cleared += 1
    return lines_cleared

# Main game loop
def main():
    tetromino = create_tetromino()
    fall_time = 0
    fall_speed = 0.5
    running = True

    while running:
        screen.fill(BLACK)
        draw_grid()
        draw_tetromino(tetromino)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino["x"] -= 1
                    if not is_valid(tetromino, grid):
                        tetromino["x"] += 1
                if event.key == pygame.K_RIGHT:
                    tetromino["x"] += 1
                    if not is_valid(tetromino, grid):
                        tetromino["x"] -= 1
                if event.key == pygame.K_DOWN:
                    tetromino["y"] += 1
                    if not is_valid(tetromino, grid):
                        tetromino["y"] -= 1
                if event.key == pygame.K_UP:
                    # Rotate tetromino
                    rotated = list(zip(*reversed(tetromino["shape"])))
                    if is_valid({"shape": rotated, "x": tetromino["x"], "y": tetromino["y"]}, grid):
                        tetromino["shape"] = rotated

        # Move tetromino down
        fall_time += clock.get_rawtime()
        if fall_time / 1000 >= fall_speed:
            tetromino["y"] += 1
            if not is_valid(tetromino, grid):
                tetromino["y"] -= 1
                merge_tetromino(tetromino, grid)
                lines_cleared = clear_lines(grid)
                tetromino = create_tetromino()
                if not is_valid(tetromino, grid):
                    running = False
            fall_time = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()