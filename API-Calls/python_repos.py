# interactive visulations showing the relative populaarity of python projects on GitHub
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

# making a API call and storing the response
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('Status code:',r.status_code)
# storing API response
response_dict=r.json()
print('Total repositories:',response_dict['total_count'])
# exploring info about repositories
repo_dicts=response_dict['items']
print('Repositories returned:',len(repo_dicts))
names,plot_dicts=[],[]
#print('\nSelected info about each repo:')
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict={
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
    #stars.append(repo_dict['stargazers_count'])
    #print('Repository:',repo_dict['html_url'])

# making visulization
my_style=LS('#333366',base_style=LCS)

my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=14
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title='Most-Starred Python Projects on GitHub'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('pic_python_repos.svg')