import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((920, 700))
clock = pygame.time.Clock()

script_dir = os.path.dirname(__file__)

image = pygame.image.load(os.path.join(script_dir, 'clock.png'))
image = pygame.transform.scale(image, (600, 600))

minute_img = pygame.image.load(os.path.join(script_dir, 'min_hand.png'))
second_img = pygame.image.load(os.path.join(script_dir, 'sec_hand.png'))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    current_time = datetime.datetime.now()
    
    minute = int(current_time.strftime("%M"))
    second = int(current_time.strftime("%S"))

    minute_angle = minute * -6 - 30
    second_angle = second * -6 - 50

    rotated_minute = pygame.transform.rotate(minute_img, minute_angle)
    rotated_second = pygame.transform.rotate(second_img, second_angle)

    screen.fill((255, 255, 255))
    screen.blit(image, (100, 100))
    screen.blit(rotated_second, (400 - rotated_second.get_width() // 2, 400 - rotated_second.get_height() // 2))
    screen.blit(rotated_minute, (400 - rotated_minute.get_width() // 2, 400 - rotated_minute.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
