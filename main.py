import pygame

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))


#Title and Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
PlayerY = 480


#RGB Value
screen.fill((0, 0, 0))
pygame.display.update()

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False