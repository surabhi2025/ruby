import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

rect1 = pygame.Rect(100, 250, 50, 80)
rect2 = pygame.Rect(600, 250, 50, 80)

speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect1.x -= speed

    if keys[pygame.K_RIGHT]:
        rect1.x += speed

    if keys[pygame.K_UP]:
        rect1.y -= speed

    if keys[pygame.K_DOWN]:
        rect1.y += speed

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 225, 0), rect2)

    pygame.display.flip()

pygame.quit()