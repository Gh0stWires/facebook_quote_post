#!/usr/bin/env python

__author__ = "Gh0st <gh0stmusc@gmail.com>"
__license__ = "GNU General Public License, version 2"

import facebook
import json
import urllib2

# Set facebook page id and access token
CFG = {"page_id": "https://www.facebook.com/<your account>/about",
       "access_token": "FACEBOOK API KEY"}
# Quote Api URL
QUOTE_URL = "https://theysaidso.p.mashape.com/quote?query=software"

# Get api related to your access token
def get_api(cfg):
    graph = facebook.GraphAPI(cfg["access_token"])

    return graph

# Retrieve a quote from the api and return it
def get_quote():

    request = urllib2.Request(QUOTE_URL, headers = {"X-Mashape-Key" : "THEYSAIDSO API KEY",
           "Accept" : "application/json"})
    resp = json.loads(urllib2.urlopen(request).read())
    q = resp['contents']['quote'].encode('ascii','ignore')
    a = resp['contents']['author'].encode('ascii','ignore')
    print q + " - " + a
    return q + " - " + a

# This is were the magic happens
def main():
    api = get_api(CFG)
    msg = get_quote()
    api.put_wall_post(msg)



if __name__ == '__main__':
    main()
