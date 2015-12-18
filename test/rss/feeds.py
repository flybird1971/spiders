#!/usr/bin/env python
#encoding:utf8

import sys,os
import feedparser
sys.path.insert(1,os.path.realpath('..'))
from utils.CollectionHelper import  CollectionHelper
# from future import Future

python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
                      "RecentChanges?action=rss_rc"

feed = feedparser.parse( python_wiki_rss_url )
print "-"*88
CollectionHelper.printEx(feed)
print CollectionHelper.getMaxDeepth()

# hit_list = [ "http://...", "...", "..." ] # list of feeds to pull down
# # pull down all feeds
# future_calls = [Future(feedparser.parse,rss_url) for rss_url in hit_list]
# # block until they are all in
# feeds = [future_obj() for future_obj in future_calls]

