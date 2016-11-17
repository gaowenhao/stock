# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
from utility import *
import urllib2
import pymongo
import json

date_start = "20161001"
date_end = "20161117"
PATTERN = "%Y%m%d"

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.workday

if __name__ == '__main__':
    date_array = []
    while True:
        if date_start == date_end:
            break
        else:
            date_array.append(date_start)
        date_start = get_tomorrow(date_start, "%Y%m%d")

    date_array_str = ",".join(date_array)

    url = 'http://apis.baidu.com/xiaogg/holiday/holiday?d=%s' % date_array_str

    req = urllib2.Request(url)
    req.add_header("apikey", "7d3965aab01dad50bda99496d16f03fe")
    resp = urllib2.urlopen(req)
    content = resp.read()
    content_map = dict(json.loads(content))
    for key, val in content_map.iteritems():
        if val == "0":
            collection.insert_one({'date': date_to_str(str_to_date(key, '%Y%m%d'),'%Y-%m-%d')})
