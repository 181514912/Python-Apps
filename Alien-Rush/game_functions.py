# stores various functions to run the game
import sys
import pygame

# manages keypress
def check_keydown_events(event,ship):
    if event.key==pygame.K_RIGHT:   # checking for right arrow key
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True

# manages key release
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:   # checking for right arrow key
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

# listening events related to keyboard and mouse
def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship)
        
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
    
# updating images on screen
def update_screen(game_set,screen,ship):
    # filling color on screen redraw
    screen.fill(game_set.bg_col)
    ship.drawme()

    # making updated screen visible
    pygame.display.flip()