# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import os
import json
import datetime
import sys

STOCK_LIST_PATH = os.path.join(os.path.join(os.path.dirname(os.getcwd()), "data"), 'stock_list.json')
RANK_PATH = os.path.join(os.path.join(os.path.dirname(os.getcwd()), "data"), 'rank_%s.txt')
SPLENDID_RANK_PATH = os.path.join(os.path.join(os.path.dirname(os.getcwd()), "data"), 'splendid_rank_%s.txt')

TODAY = datetime.datetime.now().strftime('%Y-%m-%d')


def write_stock_data(data):
    """
    写入数据到stock_list.json
    :param data: 数据
    """
    stock_list_file_write = open(STOCK_LIST_PATH, 'w')
    stock_list_file_write.write(json.dumps(data))
    stock_list_file_write.close()


def load_stock_data():
    """
    加载stock_list.json数据，并且转换成对象
        :return: stock_list obj
    """
    stock_list_file_read = open(STOCK_LIST_PATH, 'r')
    return json.loads(stock_list_file_read.read())


def write_rank_data(rank_array, date):
    """
    写出rank数据，格式rank_%date%_.txt

    :param rank_array: 数据
    :param date:  日期
    :return:
    """
    rank_file = open(RANK_PATH % date, 'w')
    for stock in rank_array:
        rank_file.write(stock[0] + " " + str(stock[1]) + "\n")
    rank_file.close()


def load_rank_data(date):
    rank_file = open(RANK_PATH % date, 'r')
    result = []
    for line in rank_file.readlines():
        result.append(line[0:6])
    rank_file.close()
    return result


def write_splendid_rank_data(data, date):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    splendid_rank_file = open(SPLENDID_RANK_PATH % date, 'w')
    for item in data:
        splendid_rank_file.write(item[0] + " " + str(item[1]) + "\n")
    splendid_rank_file.close()
