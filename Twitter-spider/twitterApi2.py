# retrieve statuses of friend from twitter and show only 50 characters
import urllib
import twurl
import json

TWITTER_URL='https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct=raw_input('Enter Twitter Account:')
    if len(acct)<1:
        break
    url=twurl.augment(TWITTER_URL,{'screen_name':acct,'count':'5'})
    print 'Fetching from',url
    conn=urllib.urlopen(url)
    data=conn.read()
    print data[:250]
    headers=conn.info().dict
    print 'Remaining',headers['x-rate-limit-remaining']
    js=json.loads(data)
    print json.dumps(js,indent=4)

    for u in js['users']:
        print u['screen_name']
        s=u['status']['text']
        print ' ',s[:50]