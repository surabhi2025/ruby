import pygame


pygame.init()


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My First Game Screen")


GREY = (58, 58, 58)


image = pygame.image.load("dog.jpg") 
image = pygame.transform.scale(image, (300, 300))


image_rect = image.get_rect(center=(250, 250))


done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(GREY)

    
    screen.blit(image, image_rect)

    
    pygame.display.update()

pygame.quit()