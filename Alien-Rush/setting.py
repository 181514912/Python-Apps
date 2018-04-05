# a class to store all settings of the game
class Settings():

    #initialising the game's settings
    def __init__(self):

        # screen settings
        self.screen_width=1200
        self.screen_height=700
        self.bg_col=(230,230,230)   #setting background color of screen RGB

        # ship settings
        self.ship_speed_factor=1.5