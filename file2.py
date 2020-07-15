import pygame
pygame.init()
screening=pygame.display.set_mode((800,600))

#Setting title and icon of game window
pygame.display.set_caption("Game")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

running=True
event=pygame.event
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #Changing the screen color
    screening.fill((0,0,160))
    #Updadting the display inside the game loop 
    pygame.display.update()