# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import tushare as ts
from utility import *

UPPER_LIMIT = 15
LOWER_LIMIT = 5

SPLENDID_RANK = {}

if __name__ == '__main__':
    df = ts.get_today_all()
    for index, row in df.iterrows():
        if LOWER_LIMIT < float(row['trade']) < UPPER_LIMIT:
            SPLENDID_RANK[row['code'] + "-" + row['name']] = float(row['changepercent'])

    splendid_rank_array = sorted(SPLENDID_RANK.iteritems(), key=lambda d: d[1], reverse=True)

    for item in splendid_rank_array:
        print item[0], item[1]

    write_splendid_rank_data(splendid_rank_array, '2016-11-16')
