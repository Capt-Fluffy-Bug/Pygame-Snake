import pygame
import time
import random

pygame.init() #pygame.init() returns a tuple listing the number of successes and failures. So you can print it too.

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #pygame.display.setmode() returns a surface object
pygame.display.set_caption('Snake')

icon = pygame.image.load('download.jpg')
pygame.display.set_icon(icon)

img = pygame.image.load('SnakeHead.png')

clock = pygame.time.Clock()

block_size = 10
appleThickness = 10
fps =60

#direction = "up"

smallfont = pygame.font.SysFont("comicsansms", 25) # returns a font obj
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Paused", black, -100, size = "large")
        message_to_screen("Press C to continue or Q to quit ", black, 25)

        pygame.display.update()
        clock.tick(4)

def score(score):
    text = smallfont.render("SCORE: "+str(score), True, black)
    gameDisplay.blit(text, [0, 0])

def randAppleGen():
    randAppleX = round(random.randrange(0,display_width-appleThickness)/10.0)*10.0 # instead of 10 you can use round( x/10.0 )*10.0
    randAppleY =round(random.randrange(0,display_height-appleThickness)/10.0)*10.0

    return randAppleX, randAppleY


def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Snake", green, y_displace = -100, size = "large")
        message_to_screen("The objective of the game is to eat the apples", black, -30)
        message_to_screen("The more apples you eat, the longer you get", black, 10)
        message_to_screen("If you run into yourself or into the boundaries, you'll die ", black, 50)
        message_to_screen("Use the arrow keys to move around. Press P to pause ", black, 90)
        message_to_screen("Press C to play or Q to quit ", black, 180)
        pygame.display.update()
        clock.tick(4)

def snake(snakelist, block_size):
##      The code below is for rotation of the snake head img if its used
##    if direction == "right":
##        head = pygame.transform.rotate(img, 270)
##    elif direction == "left":
##        head = pygame.transform.rotate(img, 90)
##    elif direction == "up":
##        head = img
##    elif direction == "down":
##        head = pygame.transform.rotate(img, 180)
##
##    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist:#[ :-1]: 
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size]) #(where to draw it, what color, [where should the left corner of obj be, width, height])
    
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    #global direction
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = -2

    snakelist = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over", red, y_displace = -50, size = "large")
            message_to_screen("Press C to play again or Q to quit", black, size = "medium", y_displace = 25 )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit =  True
                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if  event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit =  True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #direction = "left"
                    lead_x_change = -2#-block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                   # direction = "right"
                    lead_x_change = 2#block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    #direction = "up"
                    lead_x_change = 0
                    lead_y_change = -2#-block_size 
                elif event.key == pygame.K_DOWN:
                   # direction = "down"
                    lead_x_change = 0
                    lead_y_change = 2#block_size
                elif event.key == pygame.K_p:
                    pause()

    # For the boundary
        if lead_x>=display_width or lead_x <=0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

    ##      the code below is for the first level  of snake where there is no boundary and the player can infinitely move around
    ##    if lead_x >= display_width:
    ##        lead_x = 0
    ##    elif lead_x < 0:
    ##        lead_x = display_width
    ##    elif lead_y >= display_height:
    ##        lead_y = 0
    ##    elif lead_y < 0:
    ##        lead_y = display_height
        

    ##       the code below lets you move the character as long as you're holdiong the arrow key down
    ##        if event.type == pygame.KEYUP:
    ##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    ##                lead_x_change = 0
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        
        gameDisplay.fill(white)
        
        
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[ : -1 ]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(snakelist, block_size)

        score((snakeLength-1)*10)
        
        pygame.display.update()

##        if lead_x == randAppleX and lead_y == randAppleY:
##             randAppleX = random.randrange(0,display_width-block_size, 10) # instead of 10 you can use round( x/10.0 )*10.0
##             randAppleY =random.randrange(0,display_height-block_size, 10)
##             snakeLength += 1

##        if lead_x >= randAppleX and lead_x <= randAppleX + appleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + appleThickness:
##                 randAppleX, randAppleY = randAppleGen()
##                 snakeLength += 1

        if (lead_x > randAppleX) and (lead_x < randAppleX + appleThickness) or (lead_x + block_size > randAppleX) and (lead_x + block_size < randAppleX + appleThickness):
            if (lead_y > randAppleY) and (lead_y < randAppleY + appleThickness) or (lead_y + block_size > randAppleY) and (lead_y + block_size < randAppleY + appleThickness):
##                 randAppleX = random.randrange(0,display_width-appleThickness, 10) # instead of 10 you can use round( x/10.0 )*10.0
##                 randAppleY =random.randrange(0,display_height-appleThickness, 10)
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                
         

        clock.tick(fps) #defines the frames per second

        
    pygame.quit()

    quit()

game_intro()
gameLoop()
