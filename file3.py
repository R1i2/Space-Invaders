import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Adding player attributes
player=pygame.image.load("space-invaders.png")
playerX=370
playerY=470

#function to draw the player
def Fplayer():
    screen.blit(player,(playerX,playerY))

running=True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    #Adding player to display screen
    Fplayer()
    
    pygame.display.update()