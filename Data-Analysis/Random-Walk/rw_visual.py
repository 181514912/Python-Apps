import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    # make a random walk and plot the points
    rw=RandomWalk(5000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10,6))  # set the size of the plotting window

    point_no=list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,linewidth=1)
    #plt.scatter(rw.x_values,rw.y_values,c=point_no,cmap=plt.cm.Blues,edgecolors='none',s=1)
    
    # emphasizing the first and last points
    plt.scatter(0,0,c='green',edgecolors='none',s=5)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=5)

    # removing the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_run=input('Make another walk? (y/n): ')    # for python 2.x use raw_input()
    if keep_run=='n':
        break