import pygame


pygame.init()


pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Background Image and Sound")

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)      # -1 means loop forever
pygame.mixer.music.set_volume(0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.blit(background, (0, 0))

    
    pygame.display.update()


pygame.mixer.music.stop()
pygame.quit()