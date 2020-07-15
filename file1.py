import pygame

#Initialize the pygame
pygame.init()

#crate the screen
screening=pygame.display.set_mode((800,600))

#Game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
