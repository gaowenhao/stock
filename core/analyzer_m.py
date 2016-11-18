# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import pymongo

stock_array = ["600006", "600011", "600015", "600016", "600018", "600019", "600023", "600026", "600027", "600029",
               "600031", "600048", "600050", "600051", "600052", "600057", "600059", "600067", "600068", "600070",
               "600073", "600075", "600076", "600077", "600078", "600080", "600082", "600084", "600086", "600089"]

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock_k_info

if __name__ == '__main__':
    for stock_code in stock_array:
        stock_info_array = collection.find({'code': str(stock_code)})
        for index, stock_info in enumerate(stock_info_array):
            pass