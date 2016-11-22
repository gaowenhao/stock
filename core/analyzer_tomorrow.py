# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import pymongo
from utility import *
import threading

EACH_THREAD_ARRAY = 30
THREAD_POLL = []

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock_k_info

date_info_0 = "2016-11-15"
date_info_1 = "2016-11-16"
date_info_2 = "2016-11-17"

result_rank = {}


def tomorrow_rank_guess(stock_array):
    for stock_code in stock_array:
        cursor = collection.find(
            {'$and': [{'code': stock_code},
                      {'$or': [{'date': date_info_0}, {'date': date_info_1}, {'date': date_info_2}]}]})
        close0 = float(cursor[0]['close'])
        close1 = float(cursor[1]['close'])
        close2 = float(cursor[2]['close'])

        open0 = float(cursor[0]['open'])
        open1 = float(cursor[1]['open'])
        open2 = float(cursor[2]['open'])

        ma50 = float(cursor[0]['ma5'])
        ma51 = float(cursor[1]['ma5'])
        ma52 = float(cursor[2]['ma5'])

        ma100 = float(cursor[0]['ma10'])
        ma101 = float(cursor[1]['ma10'])
        ma102 = float(cursor[2]['ma10'])

        ma200 = float(cursor[0]['ma20'])
        ma201 = float(cursor[1]['ma20'])
        ma202 = float(cursor[2]['ma20'])

        result_rank[stock_code] = (ma50 - close0) + (ma100 - close0) + (ma200 - close0) + (ma51 - close1) + (
            ma101 - close1) + (ma201 - close1) + (ma52 - close2) + (ma102 - close2) + (ma202 - close2)


if __name__ == '__main__':
    stock_array = load_stock_data()
    stock_array_length = len(stock_array)

    start, end = 0, EACH_THREAD_ARRAY
    while True:
        thread = threading.Thread(target=tomorrow_rank_guess, args=(stock_array[start:end],))
        thread.start()
        THREAD_POLL.append(thread)
        if end < stock_array_length:
            start, end = end, end + EACH_THREAD_ARRAY if end + EACH_THREAD_ARRAY <= stock_array_length else stock_array_length
        else:
            break

    for thread in THREAD_POLL:
        thread.join()

    rank_array = sorted(result_rank.iteritems(), key=lambda d: d[1], reverse=True)

    for item in rank_array:
        print item[0], item[1]
