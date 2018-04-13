from random import choice

# a class to generate random walks
class RandomWalk():

    # initialising attributes of a walk
    def __init__(self,num_points=5000):
        self.num_points=num_points
        # all walks start at (0,0)
        self.x_values=[0]
        self.y_values=[0]

    # calculate all the points in the walk
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            # decide which direction to go and how far to go
            x_dir=choice([1,-1])
            x_dis=choice([0,1,2,3,4])
            x_step=x_dir*x_dis

            y_dir=choice([1,-1])
            y_dis=choice([0,1,2,3,4])
            y_step=y_dir*y_dis

            # reject moves that go nowhere
            if x_step==0 and y_step==0:
                continue

            # calculating the next x and y values
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)