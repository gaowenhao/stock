# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import tushare as ts
from utility import *
from pandas.core.frame import DataFrame
import threading
import pymongo
import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock_k_info
today = datetime.datetime.now().strftime('%Y-%m-%d')


if __name__ == '__main__':
    df = today_data = ts.get_today_all()
    for index, row in df.iterrows():
        post = {'code': row['code'], 'p_change': row['trade'] - row['open'],
                'date': today}
        collection.insert_one(post)
