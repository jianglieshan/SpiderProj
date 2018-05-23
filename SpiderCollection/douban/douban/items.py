# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    pass

class DoubanTopic(scrapy.Item):
    title = scrapy.Field()
    title_url = scrapy.Field()
    people = scrapy.Field()
    people_url = scrapy.Field()
    replay_num = scrapy.Field()
    post_time = scrapy.Field()
