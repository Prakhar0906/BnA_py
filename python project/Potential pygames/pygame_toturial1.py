import pygame
from pygame.constants import K_LEFT
#initilise pygames
pygame.init()

screen = pygame.display.set_mode((600, 600))  #width and height, center is 300

background= pygame.image.load('background2.jpg')

running = True

#title and icon, icon or image must be 32 by 32
pygame.display.set_caption("Space invaders")
'''
for icon
icon= pygame.image.load('image name')
pygame.display.set_icon(icon) #it is the variable name

'''
#player
playerimage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
player_x_change = 0

#enemy
enemy_image = pygame.image.load('alien.png')
enemyX = 370
enemyY = 280
enemyX_change = 0.3
enemyY_change = 0


def enemy_cord(x, y):
    screen.blit(enemy_image, (x, y))


def player(x, y):
    screen.blit(playerimage, (x, y))


while running:
    screen.fill((115, 33, 160))
    #background image
    #screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if a key stroke is pressed, check weather left or right
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                print("left key is pressed")
                player_x_change -= 0.5

            elif event.key == pygame.K_RIGHT:
                print("Right key is pressed")
                player_x_change += 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                print("Key is released")
                player_x_change = 0

    playerX += player_x_change
    enemyX+= enemyX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 536:
        playerX = 536
    #boundry of spaceship 

    if enemyX <= 0:
        enemyX = 0
        enemyY+= 10
        enemyX_change= 0.3
    elif enemyX >= 536: 
        enemyY+=10
        enemyX= 536 
        enemyX_change= -0.3

    player(playerX, playerY)
    enemy_cord(enemyX, enemyY)
    pygame.display.update(
    )  # importan command must in every code, refreshes the screen
