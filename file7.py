import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("space invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
running=True
player=pygame.image.load("space-invaders.png")
playerX=370
playerY=480
playerX_change=0
enemy=pygame.image.load("alien.png")
enemyX=random.randint(0,800)
enemyY=random.randint(0,150)
enemyX_change=4
enemyY_change=40

#Adding background image
background=pygame.image.load("background.png")

def Fplayer(x,y):
    screen.blit(player,(x,y))
def Fenemy(x,y):
    screen.blit(enemy,(x,y))
while running:
    screen.fill((0,0,0))

    #Adding background to workspace
    # """Note We also have to update the distance change attribute because the background image makes movement slower"""
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    enemyX+=enemyX_change
    if playerX<0:
        playerX=0
    elif playerX>736:
        playerX=736

    #Movement mechanism of space enemy
    if enemyX<=0:
        enemyX_change=4
        enemyY+=enemyY_change
    elif enemyX>=736:
        enemyX_change=-4
        enemyY+=enemyY_change
    
    Fplayer(playerX,playerY)
    Fenemy(enemyX,enemyY)
    pygame.display.update()
    