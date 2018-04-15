# API call for the IDs of the current top articles (sorted w.r.t. numbers of comments) on Hacker News
import requests
from operator import itemgetter

# making an API call and storing the response
url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print('Status code:',r.status_code)
# processing info about each submission
sub_ids=r.json()
sub_dicts=[]
for sub_id in sub_ids[:30]:
    # making a seperate API call for each submission
    url=('https://hacker-news.firebaseio.com/v0/item/'+str(sub_id)+'.json')
    sub_r=requests.get(url)
    print(sub_r.status_code)
    response_dict=sub_r.json()

    sub_dict={
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id='+str(sub_id),
        'comments':response_dict.get('descendants',0)
    }
    sub_dicts.append(sub_dict)

sub_dicts=sorted(sub_dicts,key=itemgetter('comments'),reverse=True)
for sub_dict in sub_dicts:
    print('\nTitle:',sub_dict['title'])
    print('Discussion link:',sub_dict['link'])
    print('Comments:',sub_dict['comments'])