# import scrapy
from scrapy.loader import ItemLoader
import time
import sys
sys.path.append("..")
from ..items import *
from ..DBHelper import douban_db

class DoubanSpider(scrapy.Spider):
    name = "douban"

    def __init__(self,start = 0):
        self.start = start

    def start_requests(self):
        urls = [
            'https://www.douban.com/group/haixiuzu/discussion?start=%s'%self.start,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        contents = []
        for i in range(1,len(response.css("table tr"))):
            l = ItemLoader(item= DoubanTopic(), response=response)
            l.add_xpath('title_url', '((//table//tr)[%d]//td)[1]//a//attribute::href'%(i+2))
            l.add_xpath('title', '((//table//tr)[%d]//td)[1]//a//attribute::title'%(i+2))
            l.add_xpath('people', '((//table//tr)[%d]//td)[2]//a//text()'%(i+2))
            l.add_xpath('people_url', '((//table//tr)[%d]//td)[2]//a//attribute::href'%(i+2))
            l.add_xpath('replay_num', '((//table//tr)[%d]//td)[3]//text()'%(i+2))
            l.add_xpath('post_time', '((//table//tr)[%d]//td)[4]//text()'%(i+2))
            model = l.load_item()
            contents.append(model)
        douban_db.insert_models('douban_topic',contents)
        if len(contents) == 0:
            time.sleep(600)
        url = response.url
        url_array = url.split('=')
        new_url = url_array[0] + '=' +str(int(url_array[1]) + 25)
        time.sleep(30)
        yield scrapy.Request(url=new_url,callback=self.parse)

