# a class to show information regarding scores
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():

    # initialising scorekeeping attributes
    def __init__(self,game_set,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.game_set=game_set
        self.stats=stats

        # font settings
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        # preparing the initial score images
        self.show_score()
        self.show_high_score()
        self.show_level()
        self.show_ships()

    # rendering the image of score
    def show_score(self):
        rounded_score=int(round(self.stats.score,-1))
        score_str='{:,}'.format(rounded_score)  # comma seperated scores
        self.score_img=self.font.render(score_str,True,self.text_color,self.game_set.bg_col)
        # displaying the score at top right
        self.score_rect=self.score_img.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    # rendering image of high score
    def show_high_score(self):
        high_score=int(round(self.stats.high_score,-1))
        high_score_str='{:,}'.format(high_score)
        self.high_score_img=self.font.render(high_score_str,True,self.text_color,self.game_set.bg_col)
        # centering the high score at top
        self.high_score_rect=self.high_score_img.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top

    # rendering image of game level
    def show_level(self):
        self.level_img=self.font.render(str(self.stats.level),True,self.text_color,self.game_set.bg_col)
        # setting game level position below score
        self.level_rect=self.level_img.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    # show how many ships i.e. lifes are left
    def show_ships(self):
        self.ships=Group()
        for ship_no in range(self.stats.ships_left):
            ship=Ship(self.game_set,self.screen)
            ship.rect.x=10+ship_no*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    # draw the score board
    def drawme(self):
        self.screen.blit(self.score_img,self.score_rect)
        self.screen.blit(self.high_score_img,self.high_score_rect)
        self.screen.blit(self.level_img,self.level_rect)
        self.ships.draw(self.screen)