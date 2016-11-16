# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description:  glean the large order of a stock and analyze data and save
"""

import tushare as ts
import threading
from utility import *

BUY_STR = "买盘"
SELL_STR = "买盘"
VOL = 600  # 大单界限
DIVISOR = VOL * 100  # 由于这个框架返回的结果是股，而我们这里计算的是手，所以要用手*100 得股
EACH_THREAD_ARRAY = 30
INFO_DATE = "2016-11-11"

RANK_RESULT = {}
THREAD_POLL = []


def generate_rank_result(stock_array):
    try:
        for stock in stock_array:
            score = 0
            data = ts.get_sina_dd(stock, INFO_DATE, vol=VOL)
            if data is not None:
                for index, row in data.iterrows():
                    volume = float(row['volume'])
                    score += volume / DIVISOR if row['type'] == BUY_STR else -(volume / DIVISOR)
                RANK_RESULT[data['code'][0] + "-" + data['name'][0]] = score
    except Exception as e:
        pass


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

    for thread in THREAD_POLL:
        thread.join()

    rank_array = sorted(RANK_RESULT.iteritems(), key=lambda d: d[1], reverse=True)

    for item in rank_array:
        print item[0], item[1]

    print(len(rank_array))
    write_rank_data(rank_array, INFO_DATE)
