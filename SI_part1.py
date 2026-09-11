import pygame
import random

pygame.init()


WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Example")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

player = pygame.Rect(375, 500, 50, 50)


enemies = []

for i in range(7):
    enemy = pygame.Rect(
        random.randint(0, WIDTH - 50),
        random.randint(0, HEIGHT - 50),
        50,
        50
    )
    enemies.append(enemy)

score = 0

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1

            
            enemy.x = random.randint(0, WIDTH - 50)
            enemy.y = random.randint(0, HEIGHT - 50)

    
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()