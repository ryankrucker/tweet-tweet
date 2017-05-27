import requests
import requests.auth
import oauth2
import time
import http.client
import json
import sys

if len(sys.argv) != 3:
    print ('usage : twitter-topics-request.py <Topic> <Image> \nYou must specify the topic as the first arg')
    sys.exit(1)
    
print(sys.argv[1],sys.argv[2])
url = 'https://charmerapi.herokuapp.com/api/topic'
authurl = 'https://charmerapi.herokuapp.com/connect/token'
sesssion = requests.Session()
client_id = '-KfbxwzUfetX14BLgD59'
client_secret = 'QpCWwwXdpsLCfsGt44Sz2CLtW5ud2Rnv'
grant_type = 'client_credentials'
scope = 'charm.read profile.read topic.read topic.write'
headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
post_data = {"client_id":client_id,"client_secret":client_secret,'grant_type':grant_type, 'scope':scope}
response = requests.post(authurl,data=post_data)
expires_in = response.json()['expires_in']
access_token = 'Bearer ' + response.json()['access_token']
header = {'Content-Type': 'application/json','Accept':'*/*','Authorization':access_token ,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
token_type = response.json()['token_type']
pdata = {"name":sys.argv[1],"pictureUrl":sys.argv[2],"woeid":'23424977'}
r = requests.get(url,params = {"limit":"500"} ,headers=header)
flag = 1
#print(r.headers)
#print(r.raise_for_status())
for item in r.json():
    if item['name'] == sys.argv[1]:
        if item['pictureUrl'] == sys.argv[2]:
            flag = 0
            break
if flag == 1:
    r = requests.post(url, data = json.dumps(pdata),headers=header)
    print(r.json())
else:
    print("Already Exists")         