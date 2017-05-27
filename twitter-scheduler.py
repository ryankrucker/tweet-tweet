import schedule
import time
import json
import sys
import subprocess
from pprint import pprint


def job():
    #definition
    df_dict = {}

    #call twitter sourcek
    #exec(open("twitter-topics-source.py").read(), globals())

    #parse the response
#    j = json.loads(df_dict)
    s2_out = subprocess.check_output([sys.executable, "twitter-topics-source.py"])
    fetchlist =  s2_out.decode().split('\n')
    fetchlist.pop(0)
    fetchlist.pop()
    for fetchitem in fetchlist:
        item = fetchitem.split(' ',1 )
        topic = item[1]
        topic = topic.lstrip()
        topic = topic.replace("}", "")
        sys.argv =['giphy-search-api.py',topic]
        exec(open("giphy-search-api.py").read(), globals())

    #run following inside a loop, using above array
    #Pass the single array elements to the file usin globals()
    #Use the element in place of Ronaldo
    #exec(open("google-search-api-console.py " + topic).read(), globals())

#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("0:00").do(job)
schedule.every().day.at("2:00").do(job)
schedule.every().day.at("4:00").do(job)
schedule.every().day.at("7:00").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("14:00").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("22:00").do(job)
schedule.every().day.at("23:00").do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)
