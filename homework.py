import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

font = pygame.font.Font(None, 40)
width = 200
height = 100

done = True

while done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill("white")

    text = font.render("Hi", True, "black")
    screen.blit(text, (250, 100))

    pygame.draw.rect(screen, "blue", (220, 190, width, height))

    pygame.display.update()

pygame.quit()