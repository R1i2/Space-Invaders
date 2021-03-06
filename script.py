import pygame
import random
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("space invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
player=pygame.image.load("space-invaders.png")
background=pygame.image.load('background.png')
playerX=370
playerY=480
playerX_change=0
num_of_enemies=4
enemy=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
for i in range(num_of_enemies):
    enemy.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(20)
bullet=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=-10
bullet_state="ready"
running=True

#Adding score
score_value=0
scoreX=10
scoreY=10
font=pygame.font.Font("freesansbold.ttf",32)
def showFont():
    score_text=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score_text,(scoreX,scoreY))
#Adding GAME over font
over_font=pygame.font.Font("freesansbold.ttf",64)
def gameOver():
    game_over=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over,(200,200))
#Adding background music
mixer.music.load("background.wav")
mixer.music.play(-1)

def Fplayer(x, y):
    screen.blit(player, (x, y))
def Fenemy(x, y, i):
    screen.blit(enemy[i], (x, y))
def Fbullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x+16, y+10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2)+math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    return False
def afterCollision(i):
    global bulletY,bullet_state,score_value,enemyX,enemyY
    bulletY = 480
    bullet_state = "ready"
    score_value+=1
    enemyX[i] = random.randint(0, 735)
    enemyY[i] = random.randint(50, 150)
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound=mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    Fbullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX+=playerX_change   
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    for i in range(num_of_enemies):
        Fenemy(enemyX[i], enemyY[i], i)
        if enemyY[i]>400:
            for j in range(num_of_enemies):
                enemyY[j]=2000
                gameOver()
        if enemyX[i] < 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -4
            enemyY[i]+=enemyY_change[i]
        enemyX[i]+=enemyX_change[i]
        collide = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collide:
            #Adding collision sound
            collisionSound=mixer.Sound("explosion.wav")
            collisionSound.play()
            afterCollision(i)
    #Adding score:
    showFont()
    if bulletY < 0:
        bullet_state = "ready"
        bulletY = 480
    if bullet_state is "fire":
        Fbullet(bulletX, bulletY)
        bulletY+=bulletY_change
    Fplayer(playerX, playerY)
    pygame.display.update()