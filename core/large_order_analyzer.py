# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description:
"""
import tushare as ts
from utility import *
from pandas.core.frame import DataFrame

date = '2016-10-17'
today = '2016-10-21'
result_data = {}

if __name__ == "__main__":
    stock_array = load_rank_data(date)
    for stock in stock_array[0:30]:
        df = DataFrame(ts.get_hist_data(stock, date, today))
        last_close = 0
        max = 0
        for index, row in df.iterrows():
            if index == date:
                last_close = float(row['close'])
                continue
            if float(row['high']) > max:
                max = float(row['high'])
        print stock ,max - last_close
