# -*- coding -*-

import re
import pandas as pd
import requests

def panda_parse_table(page_text):
    table_reg = re.compile('<table>.*?</table>', re.S)
    match = re.search(table_reg, page_text)
    page_text = match.group()
    dfs = pd.read_html(page_text)
    frame = dfs[0]
    file_prefix = 'shenzhen_maket_201812'
    cvs_path = '%s.cvs'%file_prefix
    frame.to_csv(cvs_path)
    print('%s has been wrote done.'%cvs_path)
    excel_path = '%s.xls'%file_prefix
    frame.to_excel('%s.xls'%file_prefix)
    print('%s has been wrote done.'%excel_path)

url = 'http://docs.static.szse.cn/www/market/periodical/month/W020181205571126320810.html' #深交所的月度交易统计表
try:
    response = requests.get(url)
    page_text = response.text
except:
    print('从深交所网站:{0:s}站获股票市场月度报表失败, 从本文件中获取表格页面字符串')
    try:
        with open('W020181205571126320810.html', 'r', encoding='GBK') as f:
            page_text = f.read()
    except:
        print('Read html failed.')
        raise(Exception)
finally:
    panda_parse_table(page_text)

