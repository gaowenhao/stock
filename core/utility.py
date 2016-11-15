# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import os
import json
import datetime

STOCK_LIST_PATH = os.path.join(os.path.join(os.path.dirname(os.getcwd()), "data"), 'stock_list.json')
RANK_PATH = os.path.join(os.path.join(os.path.dirname(os.getcwd()), "data"), 'rank_%s.txt')

TODAY = datetime.datetime.now().strftime('%Y-%m-%d')


def write_stock_data(data):
    """
    :param data: 写入的数据
    :return:
    """
    stock_list_file_write = open(STOCK_LIST_PATH, 'w')
    stock_list_file_write.write(json.dumps(data))
    stock_list_file_write.close()


def load_stock_data():
    """
        :return: stock_list obj
    """
    stock_list_file_read = open(STOCK_LIST_PATH, 'r')
    return json.loads(stock_list_file_read.read())


def write_rank_data(rank_array, date):
    rank_file = open(RANK_PATH % date, 'w')
    for stock in rank_array:
        rank_file.write(stock[0] + " " + str(stock[1]) + "\n")
    rank_file.close()
