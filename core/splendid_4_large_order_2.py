# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import pymongo
from utility import *

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.stock
collection = db.stock_k_info

result_dict = {'up': 0.0, 'low': 0.0, 'middle': 0.0}

if __name__ == '__main__':
    security_code_array = load_rank_data_all("2016-11-18")
    result = []
    for security_code in security_code_array:
        security_info = collection.find_one({'code': security_code[0:6]})
        result.append(float(security_info['high'] - float(security_info['open'])))
    for num in result:
        if num > 0:
            result_dict['up'] = result_dict['up'] + 1
        elif num == 0:
            result_dict['middle'] = result_dict['middle'] + 1
        else:
            result_dict['low'] = result_dict['low'] + 1
    print(result_dict)
