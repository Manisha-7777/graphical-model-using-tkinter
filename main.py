import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20
WHITE = (255, 255, 255)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Create paddles and ball
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Ball direction
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_w] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Ball out of bounds (reset)
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED
        ball.center = (WIDTH // 2, HEIGHT // 2)

    # Clear the window
    window.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, player1)
    pygame.draw.rect(window, WHITE, player2)
    pygame.draw.ellipse(window, WHITE, ball)

    # Draw the middle line
    pygame.draw.aaline(window, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Update the display
    pygame.display.flip()