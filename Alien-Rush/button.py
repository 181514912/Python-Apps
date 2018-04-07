# button class for the game
import pygame.font

class Button():

    # initialising button attributes
    def __init__(self,game_set,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        # setting properties of button
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        # centering the rectangle object of button
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.show_msg(msg)  # needed only once

    # centering text on the button by rendering it into image
    def show_msg(self,msg):
        self.msg_img=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_img_rect=self.msg_img.get_rect()
        self.msg_img_rect.center=self.rect.center

    # drawing the button
    def drawme(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)