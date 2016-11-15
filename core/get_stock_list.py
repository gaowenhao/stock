# encoding=utf-8
"""
    @author: gaowenhao
    @email: vevz@163.com
    @description: 
"""
import urllib
from utility import *

data_url = 'http://money.finance.sina.com.cn/d/api/' \
           'openapi_proxy.php/?__s=[["hq","hs_a","",0,%s,80]]&callback=FDC_DC.theTableData'

LIMIT = 15

if __name__ == "__main__":
    result = []
    for x in range(1, 40):
        response = urllib.urlopen(data_url % x)
        row_data = response.read()
        data = row_data[row_data.index('(') + 1: -2]
        stock_array = json.loads(data)[0]['items']

        for stock in stock_array:
            if float(stock[3]) <= LIMIT:
                result.append(stock[1])

    write_stock_data(result)
    print("------------------------  %s 以下的股票列表获取已完成。"
          "存档到 %s  ||  共 %s 条目  ------------------------" % (LIMIT, STOCK_LIST_PATH, len(result)))
