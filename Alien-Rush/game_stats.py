# class for tracking statistics for alien rush
class GameStats():
    
    # initialising statistics
    def __init__(self,game_set):
        self.game_set=game_set
        self.reset_stats()
        self.game_active=False  # starting game in inactive state
        try:
            fhand=open('temp.rdf','r')
            score=int(fhand.read()) # getting overall high score
            fhand.close()
        except:
            score=0
        self.high_score=score   # never reset this
    
    # initialising changing statistics
    def reset_stats(self):
        self.ships_left=self.game_set.ship_limit
        self.score=0
        self.level=1