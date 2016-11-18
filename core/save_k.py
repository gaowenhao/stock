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

THREAD_POLL = []
EACH_THREAD_ARRAY = 30

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock_k_info


def save_all_k(stock_array):
    for stock in stock_array:
        df = DataFrame(ts.get_hist_data(stock, start="2015-01-05", end="2016-11-18"))
        for index, row in df.iterrows():
            post = {'code': stock, 'date': index, 'open': row['open'], 'high': row['high'], 'close': row['close'],
                    'low': row['low'], 'volume': row['volume'], 'p_change': row['p_change'], 'ma5': row['ma5'],
                    'ma10': row['ma10'], 'ma20': row['ma20'], 'v_ma5': row['v_ma5'], 'v_ma10': row['v_ma10'],
                    'v_ma20': row['v_ma20'], 'turnover': row['turnover']}
            collection.insert_one(post)


if __name__ == '__main__':
    stock_array = load_stock_data()
    stock_array_length = len(stock_array)

    start, end = 0, EACH_THREAD_ARRAY
    while True:
        thread = threading.Thread(target=save_all_k, args=(stock_array[start:end],))
        thread.start()
        THREAD_POLL.append(thread)
        if end < stock_array_length:
            start, end = end, end + EACH_THREAD_ARRAY if end + EACH_THREAD_ARRAY <= stock_array_length else stock_array_length
        else:
            break
