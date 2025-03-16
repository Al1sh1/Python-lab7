import pygame
import sys
import math
import time


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")


background = pygame.image.load('clock.png')
minute_hand = pygame.image.load('arm1.png')
second_hand = pygame.image.load('arm2.png')


minute_hand = pygame.transform.scale(minute_hand, (500, 500))
second_hand = pygame.transform.scale(second_hand, (500, 500))


minute_hand_rect = minute_hand.get_rect()
second_hand_rect = second_hand.get_rect()


center = (WIDTH // 2, HEIGHT // 2)


running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, background.get_rect(center=center))

    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

   
    minute_angle = -(minutes * 6)  
    second_angle = -(seconds * 6)  

    
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)

   
    minute_hand_rect = rotated_minute_hand.get_rect(center=center)
    second_hand_rect = rotated_second_hand.get_rect(center=center)

    
    screen.blit(rotated_minute_hand, minute_hand_rect)
    screen.blit(rotated_second_hand, second_hand_rect)

    
    pygame.display.flip()

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()
