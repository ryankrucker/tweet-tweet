import requests
import http.client
import json
import sys

if len(sys.argv) != 2:
    print ('usage : giphy-search-api.py <Topic>\nYou must specify the topic as the first arg')
    sys.exit(1)
url = 'http://api.giphy.com/v1/gifs/search'
headers = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
r = requests.get(url,params = {"q":sys.argv[1],"api_key":"dc6zaTOxFJmzC"} ,headers=headers)
if len(r.json()['data']) > 0:
    if 'images' in r.json()['data'][0]:
        if 'original' in r.json()['data'][0]['images']:
            if 'url' in r.json()['data'][0]['images']['original']:
                sys.argv =['twitter-topics-request.py',sys.argv[1], r.json()['data'][0]['images']['original']['url']]
                exec(open("twitter-topics-request.py").read(), globals())
else:
    sys.argv =['google-search-api-console.py',sys.argv[1]]
    exec(open("google-search-api-console.py").read(), globals())    