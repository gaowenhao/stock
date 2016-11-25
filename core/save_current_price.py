# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import tushare as ts
import pymongo
import datetime
from utility import *
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock_k_info
today = datetime.datetime.now().strftime('%Y-%m-%d')

if __name__ == '__main__':
    df = today_data = ts.get_today_all()
    stock_list = load_stock_data()
    for stock_code in stock_list:
        stock_info = df[df.code == stock_code]
