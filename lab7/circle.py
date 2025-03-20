import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

ball_radius = 25
ball_x, ball_y = 250, 250
move_step = 20
running = True

while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_radius - move_step >= 0:
                ball_y -= move_step
            elif event.key == pygame.K_DOWN and ball_y + ball_radius + move_step <= 500:
                ball_y += move_step
            elif event.key == pygame.K_LEFT and ball_x - ball_radius - move_step >= 0:
                ball_x -= move_step
            elif event.key == pygame.K_RIGHT and ball_x + ball_radius + move_step <= 500:
                ball_x += move_step
    
    clock.tick(30)

pygame.quit()