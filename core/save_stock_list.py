# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import tushare as ts
import pymongo
from pandas.core.frame import DataFrame
from utility import *

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock

if __name__ == "__main__":
    stock_data = load_stock_data()
    df = DataFrame(ts.get_stock_basics())
    for index, row in df.iterrows():
        if index in stock_data:
            collection.insert_one({'code': index, 'name': row['name'], 'industry': row['industry'], 'area': row['area'],
                                   'outstanding': row['outstanding'], 'totals': row['totals'],
                                   'totalAssets': row['totalAssets']})

