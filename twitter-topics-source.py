import pandas as pd
import numpy as np
import tweepy
import re
import sys
import firebase


TWITTER_KEYS = {
    'consumer_key':        'nUIz60sPzdV7pmJMCTnEAFks6',
    'consumer_secret':     'u7VfuU35NDdstL2Dhdz9NSOnSMrv0fJMcwCrLhD8ilCgUDX5QE',
    'access_token_key':    '277558430-Tr9BiIZvcmI8KS7L8YsKXe1wnJ0CnFZnBsURjb8D',
    'access_token_secret': 'mmhulYiOfhIToxW1R1zazuiR7KafwZDuVtI64GJ6YRRPl'
}

def connect_twitter(client_id, client_secret):
    auth = tweepy.OAuthHandler(client_id, client_secret)
    auth.set_access_token(TWITTER_KEYS['access_token_key'], TWITTER_KEYS['access_token_secret'])
    client = tweepy.API(auth)
    return client

def get_customers_count(app):
    try:
        results = app.get('/customers', None)
        result = len(results)
        return result
    except:
        return 0

def main():
    customers_count = 0

    twitter = connect_twitter(TWITTER_KEYS['consumer_key'], TWITTER_KEYS['consumer_secret'])

    city_dict = {'US':23424977}
    #city_dict = {'chicago':2379574, 'ny':2459115, 'sf':2487956, 'la':2442047}
    #city_dict = {'austin-tx':12590014}
    trending_dict = {}
    for city in city_dict:
        trending = twitter.trends_place(city_dict[city])   #request api
        trending_list = []  # create list for each city
        for i in trending:  #for the trending in each city
            for trend in i['trends']:   # get the trend
                if not trend['tweet_volume'] == None:
                    if trend['tweet_volume'] > 0:  #if volume higher than 1000 tweets
                        trending_list.append((trend['query'], trend['tweet_volume'])) #append the querry

            trending_dict[city] = trending_list

    df_dict = {}
    for i in trending_dict:
        df_dict[i] = pd.DataFrame(trending_dict[i])
        df_dict[i].columns = ['tweet', 'count']
        df_dict[i] = df_dict[i].sort_values('count', ascending=False).reset_index()
        del df_dict[i]['count']
        del df_dict[i]['index']


    # clean up tweets
    for i in df_dict:




        # df_dict[i].tweet = df_dict[i].tweet.apply(lambda x: x.encode('utf-8')) #change to string encoding


        df_dict[i].tweet = df_dict[i].tweet.apply(lambda x: re.sub("[^a-zA-Z0-9\+]", "", x))
        df_dict[i].tweet = df_dict[i].tweet.apply(lambda x: x.replace('23', '').replace('22', '').replace('+', ' '))

    df_dict['US'].head()
    print(df_dict)

    index = 0
    # append data to firebase, uncomment for firebase support
    # for city in city_dict:
    #     current_df = df_dict[city]
    #
    #     for row in np.arange(current_df.shape[0]):
    #         tweet = current_df.ix[row][0]
    #         firebase.put('/customers', str(index), tweet, params=None, headers=None, connection=None)
    #         index += 1

main()
