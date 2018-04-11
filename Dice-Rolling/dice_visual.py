import pygal
from die import Die

die1=Die()   # creating 2 dice
die2=Die()
# making die roll and store results in a list
results=[]
for num in range(1000):
    result=die1.roll()*die2.roll()
    results.append(result)

# analyzing the results
frequencies=[]
max_result=die1.num_sides+die2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
# print(frequencies)
# visualizing the result
hist=pygal.Bar()
hist.title="Results of rolling two D6 1000 times"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')