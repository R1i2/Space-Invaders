import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("space invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
player=pygame.image.load("space-invaders.png")
enemy=pygame.image.load("alien.png")
background=pygame.image.load('background.png')
playerX=370
playerY=480
playerX_change=0
enemyX=random.randint(0,800)
enemyY=random.randint(0,150)
enemyX_change=4
enemyY_change=4

#Adding bullet its attribute and state_function
bullet=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=-10
bullet_state="ready"

running=True
def Fplayer(x,y):
    screen.blit(player,(x,y))
def Fenemy(x,y):
    screen.blit(enemy,(x,y))
def Fbullet(x,y):
    global bullet_state
    bullet_state="fire"
    #Adding 16 and 10 so that bullet is fired from the middle of the spaceship
    screen.blit(bullet,(x+16,y+10))

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    #Storing the player X value in bulletX
                    bulletX=playerX
                    Fbullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    enemyX+=enemyX_change
    if playerX<0:
        playerX=0
    elif playerX>736:
        playerX=736
    if enemyX<0:
        enemyX_change=4
        enemyY+=enemyY_change
    elif enemyX>736:
        enemyX_change=-4
        enemyY+=enemyY_change

    #Adding bullet mechanism
    #For firing multiple bullets
    if bulletY<0:
        bullet_state="ready"
        bulletY=480
    #For continously appearing on the screen
    if bullet_state is "fire":
        Fbullet(bulletX,bulletY)
        bulletY+=bulletY_change

    Fplayer(playerX,playerY)
    Fenemy(enemyX,enemyY)
    pygame.display.update()