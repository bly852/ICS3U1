import pygame
from pygame.locals import *

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

pygame.init()

# Set the width and height of the screen [width,height]
size = [800,600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test Joystick Draw")

pygame.display.toggle_fullscreen()

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()


location = [[300, 300],[500,500]]
drawColor = [[255,0,0],[0,255,0]]

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        if event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                done = True

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()


    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()


        # Drawing the circle movement

        # axis 1 is the X axis
        location[i][0] += joystick.get_axis(1) * 10
        print(joystick.get_axis(1))
        # axis 0 is the Y axis inverted
        location[i][1] -= joystick.get_axis(0) * 10
        print(joystick.get_axis(0))

        pygame.draw.circle (screen, drawColor[i], (int(location[i][0]), int(location[i][1])), 20)

        # you have access to buttons 0 to 7 for each joystick
        if joystick.get_button (0):
            drawColor[i] = [255,0,0]
        elif joystick.get_button(1):
            drawColor[i] = [0,255,0]
        elif joystick.get_button(2):
            drawColor[i] = [0,0,255]


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 30 frames per second
    clock.tick(30)

# Close the window and quit.
pygame.quit ()
