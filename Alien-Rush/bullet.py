# a class to manage bullets fired from the battle ship
import pygame
from pygame.sprite import Sprite    # used to group related elements and act collectively on them

class Bullet(Sprite):

    # creating a bullet at current position of the battle ship
    def __init__(self,game_set,screen,ship):
        super(Bullet,self).__init__()   # also super().__init__()
        self.screen=screen

        # creating a bullet rectangle at (0,0) and then setting it to correct position
        self.rect=pygame.Rect(0,0,game_set.bullet_width,game_set.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        # decimal value of bullet's position
        self.y=float(self.rect.y)

        self.color=game_set.bullet_color
        self.speed_factor=game_set.bullet_speed_factor

    # moving the bullets up the screen
    def update(self):
        self.y-=self.speed_factor   # updating decimal position of bullet
        self.rect.y=self.y  # updating rect position

    # drawing the bullet to the screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)