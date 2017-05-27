#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.
Command-line application that does a search.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import pprint
import json
import pandas as pd
import re,sys
from collections import namedtuple
from pandas import DataFrame as df_

from googleapiclient.discovery import build


if len(sys.argv) != 2:
    print ('usage : google-search-api-console.py <Topic> \nYou must specify the topic as the first arg')
    sys.exit(1)

class QueryItem(object):
    def __init__(self,dic):
        self.__dict__.update(dic)
    def __getitem__(self,name):
        return self.__dict__[name]

class QueryResult(object):
    def __init__(self,dic):
        self.__dict__.update(dic)
        self.items = [QueryItem(i) for i in self.items if type(i)==dict]
    def __getitem__(self,name):
        return self.__dict__[name]

def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyD0AqHLdHxCzPozP7tRaOpTvDTNKdmPBDA")

  res = service.cse().list(
      q=sys.argv[1],
      cx='012433308136881460059:v0gjqu5am6a',
    ).execute()
  try:
      if 'items' in res:
          item = res['items']
          for ite in item:
              if 'pagemap' in ite:
                  if 'cse_image' in ite['pagemap']:
                      #print(sys.argv[1] + " " +ite['pagemap']['cse_image'][0]['src'])
                      arg1 = sys.argv[1]
                      arg2 = ite['pagemap']['cse_image'][0]['src']
                      sys.argv =['twitter-topics-request.py',arg1, arg2]
                      exec(open("twitter-topics-request.py").read(), globals())
                      break
      else:
          print(sys.argv[1] + " No Image Found")
  except NameError:
      print(sys.argv[1] + " No Image Found")
  
if __name__ == '__main__':
  main()
