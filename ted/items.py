# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TedTalkItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    speaker = scrapy.Field()
    transcript = scrapy.Field()


XPATHS = {
    'title': '//meta[@name="title"]/@content',
    'speaker': '//meta[@name="author"]/@content',
    'transcript': '//p[@class="m-b:0"]/text()'
}
