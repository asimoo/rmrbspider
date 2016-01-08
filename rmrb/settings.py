# -*- coding: utf-8 -*-

# Scrapy settings for rmrb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'rmrb'

SPIDER_MODULES = ['rmrb.spiders']
NEWSPIDER_MODULE = 'rmrb.spiders'
FEED_URI = 'items.json'
FEED_FORMAT = 'json'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rmrb (+http://www.yourdomain.com)'
