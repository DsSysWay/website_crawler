# -*- coding: utf-8 -*-

# Scrapy settings for website_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'website_crawler'

SPIDER_MODULES = ['website_crawler.spiders']
NEWSPIDER_MODULE = 'website_crawler.spiders'

ITEM_PIPELINES = {
    'website_crawler.pipelines.WebsiteCrawlerPipeline': 300,        
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'website_crawler (+http://www.yourdomain.com)'
LOG_LEVEL = 'DEBUG'
