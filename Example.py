#I have imported pygame.
#I have also import random to generate random numbers.

import pygame
import random

# I am going to initialize the pygame.

pygame.init()

# I need to give my game screen a height and width.

screen_width = 900
screen_height = 350
screen = pygame.display.set_mode((screen_width,
                                  screen_height))  # This creates the screen and gives it the width and height specified as a 2 item sequence.

# I will be loading my game images which is hero 1 and all three enemy images

player = pygame.image.load("hero1.png")
enemy = pygame.image.load("enemy1.png")
enemy1 = pygame.image.load("enemy2.png")
enemy2 = pygame.image.load("enemy3.png")
prize = pygame.image.load ("prize.png")

# I want to get all my images width and height so that it can stay within the game windows width and height
image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy_height = enemy1.get_height()
enemy_width = enemy1.get_width()
enemy_height = enemy2.get_height()
enemy_width = enemy2.get_width()

#We are testing to see what is the height/width of the player

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# this is the psosition at which my hero character needs to start at.

playerXPosition = 50
playerYPosition = 25

# I have q random enemy start position and for the other 2 enemies I have started them in a place they should start.

enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)
enemy1Xposition = 500
enemy1Yposition = 10
enemy2Xposition = 700
enemy2Yposition = 50

#This will be the prize position
prizeXposition = 1000
prizeYposition = 10

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False.
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other.

keyUp = False
keyDown = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

while 1:  # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later.

    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition,
                         playerYPosition))  # This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy1,(enemy1Xposition, enemy1Yposition))
    screen.blit(enemy2,(enemy2Xposition,enemy2Yposition ))
    screen.blit(prize, (prizeXposition,prizeYposition))


    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.

            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:
    #I have added 2 more enemies to see if the hero will collide with them
    # and a prize if the hero collides with the prize he should win

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemy:

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    enemyBox2 = pygame.Rect(enemy1.get_rect())
    enemyBox2.top = enemy1Yposition
    enemyBox2.left = enemy1Xposition
    enemyBox3 = pygame.Rect(enemy2.get_rect())
    enemyBox3.top = enemy2Yposition
    enemyBox3.left = enemy2Xposition
    prizeBox= pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYposition
    prizeBox.left = prizeXposition

    # Test collision of the boxes:

    if playerBox.colliderect(enemyBox) :
        print("collide")

    # Display losing status to the user:

        print("You lose!")


        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBox2) :

    # Display losing status to the user:

        print("You lose!")


        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBox3) :

    # Display losing status to the user:

        print("You lose!")


        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox) :

    # Display winning status to the user:

        print("You Win!")


        pygame.quit()
        exit(0)




    # Make enemy approach the player.
    # I have added 2 more enemies and a prize and have given them different speeds to approach

    enemyXPosition -= 0.30
    enemy1Xposition -= 0.15
    enemy2Xposition -= 0.15
    prizeXposition  -= 0.15


    # ================The game loop logic ends here. =============
