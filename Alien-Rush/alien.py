# a class to represent individual alien from its fleet
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    # initialising alien and its starting position
    def __init__(self,game_set,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.game_set=game_set

        # loading alien image
        self.image=pygame.image.load('images/alien2.png')
        self.rect=self.image.get_rect()

        # each new alien start near top-left of screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)   # alien's exact position

    # drawing alien at its current location
    def drawme(self):
        self.screen.blit(self.image,self.rect)
    
    # if alien is at edge of screen then returns true
    def check_edge(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    
    # move alien right
    def update(self):
        self.x+=(self.game_set.alien_speed_factor*self.game_set.fleet_direction)
        self.rect.x=self.x