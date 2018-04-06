# class for tracking statistics for alien rush
class GameStats():
    
    # initialising statistics
    def __init__(self,game_set):
        self.game_set=game_set
        self.reset_stats()
        self.game_active=True
    
    # initialising changing statistics
    def reset_stats(self):
        self.ships_left=self.game_set.ship_limit