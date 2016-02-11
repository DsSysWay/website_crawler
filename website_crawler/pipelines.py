# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, select,update
from website_crawler.misc.log import *
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class WebsiteCrawlerPipeline(object):

    def __init__(self):
        self.result = codecs.open("story_result", 'a', encoding='utf-8')
    def process_item(self, item, spider):
        #info("item to db:"+ item['title'])
        content = item['viewCount'] + " " + item['head'] + " " + item['link'] +  "\n"
        self.result.write(content)
        self.result.flush()
        return item
