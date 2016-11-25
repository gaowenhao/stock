# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
from utility import *
import tushare as ts

if __name__ == '__main__':
    today_all_security_info = ts.get_today_all()
    stock_code_array = load_stock_data()
    for stock_code in stock_code_array:
        # 买入 今天开盘小于昨天最低价，昨天没有跌停的，今天开盘价不是跌停的
        yesterday_security_info = ts.get_hist_data(stock_code, start='2016-11-24', end='2016-11-24')
        today_security_info = today_all_security_info[today_all_security_info.code == stock_code]
        try:
            if float(today_security_info['open'].values[0]) < float(yesterday_security_info['low'].values[0]) and \
                            yesterday_security_info['p_change'].values[0] > -8.5 and \
                            yesterday_security_info['p_change'].values[0] > -8.5:
                print stock_code, today_security_info.name
        except (Exception) as e:
            print 'exception occur'
