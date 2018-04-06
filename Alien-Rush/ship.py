# class to manage player's ship's behavior
import pygame

class Ship():

    # initialising the ship and setting its stating position
    def __init__(self,game_set,screen):
        self.screen=screen
        self.game_set=game_set

        # loading the ship's image
        self.image=pygame.image.load('images/battle_ship.png')  # loading battle ship image
        self.rect=self.image.get_rect()     # rect means 'reactangle'
        self.screen_rect=screen.get_rect()

        # positioning ship at the bottom center
        self.rect.centerx=self.screen_rect.centerx  # setting x coordinate of ship's centre
        self.rect.bottom=self.screen_rect.bottom    # setting y coordinate of ship's bottom

        # retrieving ship's center in decimal
        self.center=float(self.rect.centerx)
        
        # movement flags
        self.moving_right=False
        self.moving_left=False
    
    # update the ship's position based on the movement flag
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.game_set.ship_speed_factor    # moving battle ship to right
        if self.moving_left and self.rect.left>0:
            self.center-=self.game_set.ship_speed_factor    # moving battle ship to left

        # update rect object
        self.rect.centerx=self.center
    
    # drawing ship at its current position
    def drawme(self):
        self.screen.blit(self.image,self.rect)

    # center the ship on screen
    def center_ship(self):
        self.center=self.screen_rect.centerx
