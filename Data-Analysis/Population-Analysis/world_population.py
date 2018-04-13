import json
import pygal
from pygal.maps.world import World
from pygal.style import LightColorizedStyle,RotateStyle
from country_codes import get_country_code

# loading the data into a list
fname='population_data.json'
with open(fname) as f:
    pop_data=json.load(f)
# building a dictionary of population data
cc_pop={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
        code=get_country_code(country_name)
        if code:
            cc_pop[code]=population

# grouping countries into 3 population levels
cc_pop1,cc_pop2,cc_pop3={},{},{}
for cc,pop in cc_pop.items():
    if pop<10000000:
        cc_pop1[cc]=pop
    elif pop<1000000000:
        cc_pop2[cc]=pop
    else:
        cc_pop3[cc]=pop

print(len(cc_pop1),len(cc_pop2),len(cc_pop3))   # seeing length of each population levels
wm_style=RotateStyle('#336699',base_style=LightColorizedStyle)
wm=World(style=wm_style)
# wm=World()
wm.title='World population in 2010, by country'
wm.add('0-10m',cc_pop1)
wm.add('10m-1bm',cc_pop2)
wm.add('>1bm',cc_pop3)
wm.render_to_file('world_pic.svg')