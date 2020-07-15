import pygame
import random
import math
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
enemyX=random.randint(0,735)
enemyY=random.randint(50,150)
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

#To calculate the score 
score=0

def Fplayer(x,y):
    screen.blit(player,(x,y))
def Fenemy(x,y):
    screen.blit(enemy,(x,y))
def Fbullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))

#Function to check whether collision has happen
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance<27:
        return True
    return False
#After collision
def afterCollision():
    global enemyX,enemyY,bulletX,bulletY,bullet_state,score
    bulletY=480
    bullet_state="ready"
    score+=1
    enemyX=random.randint(0,735)
    enemyY=random.randint(50,150)

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
    if bulletY<0:
        bullet_state="ready"
        bulletY=480
    if bullet_state is "fire":
        Fbullet(bulletX,bulletY)
        bulletY+=bulletY_change
    
    #Inserting the collison mechanism
    collide=isCollision(enemyX,enemyY,bulletX,bulletY)
    if collide:
        afterCollision()
    
    Fplayer(playerX,playerY)
    Fenemy(enemyX,enemyY)
    pygame.display.update()