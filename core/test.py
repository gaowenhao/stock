# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import pymongo
import tushare as ts

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock_k_info

date_info_1 = "2016-11-17"
date_info_2 = "2016-11-18"


class Java(object):
    @staticmethod
    def do1():
        Java.do2()

    @staticmethod
    def do2():
        pass
