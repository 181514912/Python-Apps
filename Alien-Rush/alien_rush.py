# main file of the game...staring point
import pygame   # module containing functionalities needed to make the game
from setting import Settings
from ship import Ship
import game_functions as gfs

def run_game():
    # game initialisation and screen object creation
    pygame.init()   # initialising background settings
    game_set=Settings()
    screen=pygame.display.set_mode((game_set.screen_width,game_set.screen_height))  # creating a display window i.e. screen of 1200 X 800 pixels
    pygame.display.set_caption("Alien Invasion")

    # making a ship
    ship=Ship(game_set,screen)
    
    # main loop
    while True:
        gfs.check_events(ship)
        ship.update()
        gfs.update_screen(game_set,screen,ship)       

run_game()