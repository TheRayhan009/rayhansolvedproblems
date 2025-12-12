import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("rayhan")

# Load images
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.topleft = (width // 4, height // 2)

enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_speed = 5
enemy_rect.topleft = (width, 0)

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (width, height))

# Set up game variables
gravity = 1
jump_speed = 15  # Adjusted jump speed
player_speed = 5

score = 0
font = pygame.font.Font(None, 36)

pipes = []

# Function to generate pipes
def generate_pipe():
    pipe_height = random.randint(50, height - 200)
    top_pipe_rect = enemy_image.get_rect(topleft=(width, pipe_height - 400))
    bottom_pipe_rect = enemy_image.get_rect(topleft=(width, pipe_height + 150))
    pipes.append((top_pipe_rect, bottom_pipe_rect))
# Event handling
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            gravity = -jump_speed

# Update game state
player_rect.y += gravity
gravity += 1  # Add gravity back to simulate continuous falling

if player_rect.y > height - player_rect.height:
    player_rect.y = height - player_rect.height
    gravity = 0  # Reset gravity when the player hits the ground

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player_rect.y -= jump_speed  # Adjusted the position for jumping

    # Update game state
    player_rect.y += gravity
    if player_rect.y > height - player_rect.height:
        player_rect.y = height - player_rect.height

    enemy_rect.x -= enemy_speed

    if enemy_rect.x < 0:
        enemy_rect.x = width
        generate_pipe()
        score += 10

    for pipe_pair in pipes:
        for pipe in pipe_pair:
            pipe.x -= enemy_speed

    # Check for collisions
    if (
        player_rect.colliderect(enemy_rect)
        or any(pipe_pair[0].colliderect(player_rect) or pipe_pair[1].colliderect(player_rect) for pipe_pair in pipes)
        or player_rect.y < 0
    ):
        # Reset game state on collision
        player_rect.topleft = (width // 4, height // 2)
        pipes = []
        score = 0

    # Draw everything
    screen.blit(background_image, (0, 0))  # Draw the background
    screen.blit(player_image, player_rect.topleft)  # Draw the player
    screen.blit(enemy_image, enemy_rect.topleft)  # Draw the pipes

    for pipe_pair in pipes:
        for pipe in pipe_pair:
            screen.blit(enemy_image, pipe.topleft)

    # Display score
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Generate new pipes
    if len(pipes) < 3:
        generate_pipe()

    # Update the display
    pygame.display.flip()

    # Control the game speed
    pygame.time.Clock().tick(60)
