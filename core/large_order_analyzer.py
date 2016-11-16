# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import tushare as ts
from utility import *
from pandas.core.frame import DataFrame

date = '2016-11-07'
today = '2016-11-16'
result_data = {}

if __name__ == "__main__":
    # stock_array = load_rank_data(date)
    # for stock in stock_array:
    #     ts.get_hist_data(code=stock, start=date, end=today):
    #
    df = DataFrame(ts.get_hist_data('600275', date, today))
    result_pair = []
    for index, row in df.iterrows():
        if index == date:
            result_pair.append(row['close'])
        else:
            pass
    print(result_pair)
