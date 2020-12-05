'''
Author: your name
Date: 2020-12-02 16:39:05
LastEditTime: 2020-12-05 20:04:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /analystock/analystock/pipelines.py
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import os
import datetime

header = ['序号', '代码', '名称', '最新价', '今日主力净占比 %', '今日排名', '今日涨跌 %', '5日主力净占比 %',
          '5日排名', '5日涨跌 %', '10日主力净占比 %', '10日排名', '10日涨跌 %', '所属板块', '板块代码']  # 数据列名

filename = "stock-data-"+datetime.datetime.now().strftime('%Y-%m-%d')+".csv"


class AnalystockPipeline:

    def __init__(self):

        # 每一天的数据都保存在不同的csv中，文件命名为当前日期
        if os.path.isfile("./data/"+filename):
            pass
        else:
            with open("./data/"+filename, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
            f.close()

    def process_item(self, item, spider):
        
        stock = [item['rank'], item['code'], item['name'], item['newpiece'], item['todaymain'], item['todayrank'], item['todaytrend'],
                 item['fivemain'], item['fiverank'], item['fivetrend'], item['tenmain'], item['tenrank'], item['tentrend'], item['plate'], item['platecode']]

        # 写入csv文件
        with open("./data/"+filename, 'a+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(stock)
        f.close()

        return item
