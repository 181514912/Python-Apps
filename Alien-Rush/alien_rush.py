# main file of the game...staring point
import pygame   # module containing functionalities needed to make the game
from pygame.sprite import Group # for grouping all the live bullets
from setting import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gfs

def run_game():
    # game initialisation and screen object creation
    pygame.init()   # initialising background settings
    game_set=Settings()
    screen=pygame.display.set_mode((game_set.screen_width,game_set.screen_height))  # creating a display window i.e. screen of 1200 X 800 pixels
    pygame.display.set_caption("Alien Rush")
    stats=GameStats(game_set)   # for storing game statistics

    ship=Ship(game_set,screen)  # making a ship
    bullets=Group() # for storing all bullets
    aliens=Group()  # for storing fleet of aliens
    gfs.create_fleet(game_set,screen,ship,aliens)  # creating alien's fleet
    
    # main loop
    while True:
        gfs.check_events(game_set,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gfs.update_bullets(game_set,screen,ship,aliens,bullets)
            gfs.update_aliens(game_set,stats,screen,ship,aliens,bullets)
        gfs.update_screen(game_set,screen,ship,aliens,bullets)       

run_game()