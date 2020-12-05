'''
Author: your name
Date: 2020-12-02 16:39:05
LastEditTime: 2020-12-04 17:58:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /analystock/analystock/items.py
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnalystockItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    newpiece = scrapy.Field()
    todaymain = scrapy.Field()
    todayrank = scrapy.Field()
    todaytrend = scrapy.Field()
    fivemain = scrapy.Field()
    fiverank = scrapy.Field()
    fivetrend = scrapy.Field()
    tenmain = scrapy.Field()
    tenrank = scrapy.Field()
    tentrend = scrapy.Field()
    plate = scrapy.Field()
    platecode = scrapy.Field()
