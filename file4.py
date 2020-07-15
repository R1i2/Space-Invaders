import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("space invaders")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
running=True
player=pygame.image.load('space-invaders.png')
playerX=370
playerY=480
playerX_change=0
def Fplayer(x,y):
    screen.blit(player,(x,y))
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #pygame eventkey logging
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
            elif event.key==pygame.K_RIGHT:
                playerX_change=0.3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    if playerX<0:
        playerX=0
    elif playerX>736:
        playerX=736
    
    Fplayer(playerX,playerY)
    pygame.display.update()
        