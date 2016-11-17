# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description:  glean the large order of a stock and analyze data and save
"""

import tushare as ts
import threading
from utility import *
import pymongo

BUY_STR = "买盘"
SELL_STR = "买盘"
VOL = 500  # 大单界限
DIVISOR = VOL * 100  # 由于这个框架返回的结果是股，而我们这里计算的是手，所以要用手*100 得股
EACH_THREAD_ARRAY = 50

THREAD_POLL = []

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
large_order_rank_collection = db.large_order_rank
work_day_collection = db.workday
large_order_collection = db.large_order

available_date_array = []

date_result = work_day_collection.find({}, sort=[('date', pymongo.ASCENDING,)])
for date_item in date_result:
    available_date_array.append(date_item['date'])


def generate_rank_result(stock_array):
    """获取每只股票(self)当日的大单排行榜前30，并且获取self 5日内最高点，然后用 self当日的收盘价 - self5日内最高价，存到数据库"""
    for available_date in available_date_array:
        rank_result = {}  # 存储当天所有股票的大单
        for stock in stock_array:
            score = 0
            data = ts.get_sina_dd(stock, available_date, vol=VOL)
            if data is not None:
                for index, row in data.iterrows():
                    volume = float(row['volume'])
                    score += volume / DIVISOR if row['type'] == BUY_STR else -(volume / DIVISOR)
                rank_result[data['code'][0] + "-" + data['name'][0]] = score
        rank_array = sorted(rank_result.iteritems(), key=lambda d: d[1], reverse=True)[0:30]
        if len(rank_array) > 0:
            for item in rank_array:
                large_order_collection.update({'date': available_date},
                                              {'$set': {'date': available_date},
                                               '$addToSet': {'rank': {'name': item[0], 'score': item[1]}}},
                                              True)
        print(available_date)


if __name__ == "__main__":
    stock_array = load_stock_data()
    stock_array_length = len(stock_array)

    start, end = 0, EACH_THREAD_ARRAY

    while True:
        thread = threading.Thread(target=generate_rank_result, args=(stock_array[start:end],))
        thread.start()
        THREAD_POLL.append(thread)
        if end < stock_array_length:
            start, end = end, end + EACH_THREAD_ARRAY if end + EACH_THREAD_ARRAY <= stock_array_length else stock_array_length
        else:
            break
