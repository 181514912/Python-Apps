import pygal
from die import Die

die=Die()   # creating a die
# making die roll and store results in a list
results=[]
for num in range(1000):
    result=die.roll()
    results.append(result)

# analyzing the results
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
# print(frequencies)
# visualizing the result
hist=pygal.Bar()
hist.title="Results of rolling a D6 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')