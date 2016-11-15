# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import tushare as ts

if __name__ == "__main__":
    df = ts.get_stock_basics()
    for x in df:
        print(df[x])
