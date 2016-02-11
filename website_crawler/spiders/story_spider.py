#coding="utf-8"
import  re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from website_crawler.items import *
from website_crawler.misc.log import *
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


###URL2_ARTICLE_TITLE = {}

class websiteCrawlerSpider(CrawlSpider):



    name = "website_crawler" #here is the key to name spider,if not match will throw spider not found error
    allowed_domains = ["wittyfeed.com"]
    start_urls = [
            "http://www.wittyfeed.com/story",
    ]
    rules = [
    #    Rule(sle(allow=("/followees")), follow=True, callback='parse_follow'),
    ]


    




    def __init__(self):
        info('init start')
        return

    def start_requests(self): 
        info("start url:"+ self.start_urls[0])
        yield  scrapy.Request(url=self.start_urls[0],callback=self.parse_story);


    def get_story_id(self, link):
        data = link.split("story/")
        idstr = data[1]
        info("id str:" + idstr)
        storyId = idstr.split("/") 
        info("story id:" + storyId[0])
        return  storyId[0]

    def get_response_story_id(self, link):
        data = link.split("get_view_count/")
        info("response story id:" + data[1])
        return data[1] 


    itemDict = dict()

    def parse_view(self,response):
        info("story vew url:"+ response.url)
        storyId = self.get_response_story_id(response.url)
        item = self.itemDict[storyId] 
        body = str(response.body)
        item["viewCount"]  = body.split("\n")[0]
        info("view :"+ str(item['viewCount']) + ' ' + "head:" + item['head'] + " " + item['link'] )
        return item

    def parse_story(self,response):
        info("story rsp url:"+ response.url);
        selectorList = response.xpath("//div[@class='col-lg-6 col-md-6 col-sm-6 col-xs-12 home_story_wrapper']")
        for   selector in selectorList:

            item = WebsiteCrawlerItem()
            link = selector.xpath("./div[@class='home_story_title']/h2/a/@href")
            info("link :"+ str(link))
            item['link'] = str(link.extract())
            head = selector.xpath("./div[@class='home_story_title']/h2/a/text()")
            info("head :"+ str(head))
            item['head'] = str(head.extract())
            storyId = self.get_story_id(str(link))
            self.itemDict[storyId] = item
            viewUrl = "http://stats.wittyfeed.com/get_view_count/" + storyId
            yield  scrapy.Request(url=viewUrl,callback=self.parse_view)





    def _process_request(self, request):
        info('process ' + str(request))
        return request

