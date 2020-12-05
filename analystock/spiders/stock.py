'''
Author: your name
Date: 2020-12-02 17:09:20
LastEditTime: 2020-12-04 20:01:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /analystock/analystock/spiders/stock.py
'''
import scrapy
import json
from analystock.items import AnalystockItem


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['data.eastmoney.com']
    start_urls = ['http://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=50&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f184&fid0=f4001&fields=f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&rt=53563669&cb=jQuery18305043185748388488_1606910076373&_=1606910077202',
                  'http://push2.eastmoney.com/api/qt/clist/get?pn=2&pz=50&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f184&fid0=f4001&fields=f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&rt=53563669&cb=jQuery18305043185748388488_1606910076373&_=1606910077202',
                  'http://push2.eastmoney.com/api/qt/clist/get?pn=3&pz=50&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f184&fid0=f4001&fields=f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&rt=53563669&cb=jQuery18305043185748388488_1606910076373&_=1606910077202',
                  'http://push2.eastmoney.com/api/qt/clist/get?pn=4&pz=50&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f184&fid0=f4001&fields=f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&rt=53563669&cb=jQuery18305043185748388488_1606910076373&_=1606910077202',
                  'http://push2.eastmoney.com/api/qt/clist/get?pn=5&pz=50&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f184&fid0=f4001&fields=f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&rt=53563669&cb=jQuery18305043185748388488_1606910076373&_=1606910077202']

    def parse(self, response):
        jsonstr = json.loads(response.text.split('(')[1].split(')')[0])
        stocks = jsonstr['data'].get('diff')
        items = []
        for i in range(0, len(stocks)):
            item = AnalystockItem()
            item['rank'] = stocks[i]['f225']
            item['code'] = stocks[i]['f12']
            item['name'] = stocks[i]['f14']
            item['newpiece'] = stocks[i]['f2']
            item['todaymain'] = stocks[i]['f184']
            item['todayrank'] = stocks[i]['f225']
            item['todaytrend'] = stocks[i]['f3']
            item['fivemain'] = stocks[i]['f165']
            item['fiverank'] = stocks[i]['f263']
            item['fivetrend'] = stocks[i]['f109']
            item['tenmain'] = stocks[i]['f175']
            item['tenrank'] = stocks[i]['f264']
            item['tentrend'] = stocks[i]['f160']
            item['plate'] = stocks[i]['f100']
            item['platecode'] = stocks[i]['f265']
            items.append(item)
        return items
