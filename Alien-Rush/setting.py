# a class to store all settings of the game
class Settings():

    #initialising the game's settings
    def __init__(self):

        # screen settings
        self.screen_width=1200
        self.screen_height=700
        self.bg_col=(230,230,230)   #setting background color of screen RGB , sky-blue=(135,206,250)

        # ship settings
        self.ship_limit=3   # total life

        # bullet settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color= 60,60,60
        self.bullets_allowed=3

        # alien settings
        self.fleet_drop_speed=10

        # game speed up rate
        self.speedup_scale=1.25
        self.score_scale=1.5

        self.initialize_dynamic_settings()
    
    # initializing settings that change throughout the game
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1  # right=1, left=-1
        self.alien_points=50
    
    # increasing speed on level up
    def inc_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)