import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))


sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((50, 50))
sprite1.image.fill((255, 0, 0))
sprite1.rect = sprite1.image.get_rect()
sprite1.rect.x = 100
sprite1.rect.y = 200


sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((50, 50))
sprite2.image.fill((0, 0, 255))
sprite2.rect = sprite2.image.get_rect()
sprite2.rect.x = 300
sprite2.rect.y = 200


sprites = pygame.sprite.Group(sprite1, sprite2)


CHANGE_COLOR = pygame.USEREVENT + 1


pygame.event.post(pygame.event.Event(CHANGE_COLOR))

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            sprite1.image.fill((0, 255, 0))      
            sprite2.image.fill((255, 255, 0))    

    screen.fill((255, 255, 255))
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()