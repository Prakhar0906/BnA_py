import pygame
import random 
pygame.init()

screen = pygame.display.set_mode((800, 600))  #width and height, center is 300

running= True 

pygame.display.set_caption("Space invaders")

icon= pygame.image.load('alien.png')
pygame.display.set_icon(icon) #it is the variable name

#player
playerimage = pygame.image.load('spaceship.png')
playerX, playerY = 370, 480

#enemy
enemyimage= pygame.image.load('alien.png')
enemyX, enemyY= random.randint(0, 800), random.randint(50, 150)

player= lambda x,y: screen.blit(playerimage, (x, y))

enemy= lambda x,y: screen.blit(enemyimage, (x, y))

change= 0

while running:
    screen.fill((123,122,144))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            #print("1 A key is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right key Pressed")
                change= 0.5

            elif event.key == pygame.K_LEFT:
                print("Left key is pressed")
                change= -0.5
             
        if event.type == pygame.KEYUP:
            #print("0 A key is released")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                change=0
    
    if playerX >= 736 :
        playerX = 736
    elif playerX <= 0:
        playerX=0

    playerX += change   
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()