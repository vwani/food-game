# import modules
import pygame
import sys
import random
import math

# initialise pygame
pygame.init()

# screen dimensions
res = (800, 800)

# create screen
screen = pygame.display.set_mode(res)

# title
pygame.display.set_caption('FOODIE !!')

# icon
icon = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\icon.png')
pygame.display.set_icon(icon)

# background image
backdrop = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\backdrop.png')

# font
font = pygame.font.Font('freesansbold.ttf', 36)

# player
PlayerImg = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\MalePlayer.png')

PlayerX = 336
PlayerY = 662
PlayerChangeX = 0
PlayerChangeY = 0

def player(x, y):
    screen. blit(PlayerImg, (x, y))

# healthy food

HealthyFoodNum = 3

HealthyFood1 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\HealthyFood1.png')
HealthyFood2 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\HealthyFood2.png')
HealthyFood3 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\HealthyFood3.png')
HealthyFood4 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\HealthyFood4.png')
HealthyFoodArr = [HealthyFood1, HealthyFood2, HealthyFood3, HealthyFood4]

HealthyFoodX = []
HealthyFoodY = []

for i in range(len(HealthyFoodArr)):
    num = random.randrange(10,736,100)
    if num in HealthyFoodX:
        while num in HealthyFoodX:
            num = random.randrange(10,736,100)
    HealthyFoodX.append(num)
    HealthyFoodY.append(random.randint(10,100))

# unhealthy food

UnHealthyFoodNum = 1

UnHealthyFood1 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\UnHealthyFood1.png')
UnHealthyFood2 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\UnHealthyFood2.png')
UnHealthyFood3 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\UnHealthyFood3.png')
UnHealthyFood4 = pygame.image.load('F:\\Vinaya\\Python Projects\\game\\Media\\UnHealthyFood4.png')
UnHealthyFoodArr = [UnHealthyFood1, UnHealthyFood2, UnHealthyFood3, UnHealthyFood4]

UnHealthyFoodX = []
UnHealthyFoodY = []

for i in range(len(UnHealthyFoodArr)):
    num = random.randrange(10,736,100)
    if num in HealthyFoodX:
        while num in HealthyFoodX:
            num = random.randrange(10,736,100)
    UnHealthyFoodX.append(random.randrange(10, 736, 100))
    UnHealthyFoodY.append(random.randint(10,100))

FoodChangeX = 0
FoodChangeY = 0.5

FoodArr = [HealthyFood1, HealthyFood2, HealthyFood3, HealthyFood4, UnHealthyFood1, UnHealthyFood2, UnHealthyFood3, UnHealthyFood4]

def food(img, x, y):
    screen.blit(img, (x, y))

# collision
def IsCollision(PX, PY, FX, FY):
    distX = PX+20<=FX<=PX+108
    distY = PY+20<=FY<=PY+108
    return distX and distY

# health
health = 10

def DisplayHealth(x):
    screen.blit(font.render('Health: '+str(x), True, (255, 255, 255)), (0, 0))

# game loop
running = True
while running:

    # event check
    for event in pygame.event.get():

        # exit game loop 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                PlayerChangeX = 0.2

            elif event.key == pygame.K_LEFT:
                PlayerChangeX = -0.2

    # food movement
    ''' num = random.randint(0,4) '''
    
    for i in range(len(HealthyFoodArr)):
        HealthyFoodY[i] += FoodChangeY

        if HealthyFoodY[i]>=736:
            HealthyFoodY[i] = 0
            num = random.randrange(10, 736, 100)
            while num in HealthyFoodX:
                num = random.randrange(10, 736, 100)
            HealthyFoodX[i] = num

        # collision
        collision = IsCollision(PlayerX, PlayerY, HealthyFoodX[i], HealthyFoodY[i])
        if collision:
            HealthyFoodY[i] = 0
            num = random.randrange(10, 736, 100)
            while num in HealthyFoodX:
                num = random.randrange(10, 736, 100)
            HealthyFoodX[i] = num

            health += 1
            

    # player movement
    PlayerX += PlayerChangeX

    if PlayerX >= 800-128:
        PlayerX = 800-128

    elif PlayerX <= 0:
        PlayerX = 0

    # background image
    screen.blit(backdrop, (0, 0))

    # display health
    DisplayHealth(health)

    # motion
    player(PlayerX, PlayerY)

    for i in range(len(HealthyFoodArr)):
        food(HealthyFoodArr[i], HealthyFoodX[i], HealthyFoodY[i])
    
    # update screen
    pygame.display.update()
