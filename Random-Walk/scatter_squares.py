import matplotlib.pyplot as plt

x_values=list(range(1,1001)) # [1,2,3,4,5]
y_values=[x**2 for x in x_values]   # [1,4,9,16,25]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)    # c='red' or (0,0,0.8)

# setting chart title and axes label
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

# setting size of tick labels
plt.tick_params(axis='both',which='major',labelsize=14)

# setting range for each axis
plt.axis([0,1100,0,1100000])

plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()
