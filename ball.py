import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
BALL_SPEED = 20

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - BALL_RADIUS - BALL_SPEED >= 0:
                    ball_y -= BALL_SPEED
            elif event.key == pygame.K_DOWN:
                if ball_y + BALL_RADIUS + BALL_SPEED <= HEIGHT:
                    ball_y += BALL_SPEED
            elif event.key == pygame.K_LEFT:
                if ball_x - BALL_RADIUS - BALL_SPEED >= 0:
                    ball_x -= BALL_SPEED
            elif event.key == pygame.K_RIGHT:
                if ball_x + BALL_RADIUS + BALL_SPEED <= WIDTH:
                    ball_x += BALL_SPEED

    pygame.display.flip()

pygame.quit()
sys.exit()
