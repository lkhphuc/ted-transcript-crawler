# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ted.items import TedTalkItem, XPATHS
import re


class TedCrawlSpider(CrawlSpider):
    name = 'ted_crawl'
    allowed_domains = ['ted.com']
    start_urls = ['https://www.ted.com/talks']

    pagexp = r'//a[@class="pagination__item pagination__link"]'
    talkxp = r'//div[@class="media__image media__image--thumb talk-link__image"]'

    rules = [
        Rule(LinkExtractor(allow=r'\?page=\d', restrict_xpaths=pagexp),
            follow=True),
        Rule(LinkExtractor(allow=r'talks\/[a-z_]+', restrict_xpaths=talkxp),
            callback='parse_page')
    ]

    def parse_web(self, response):
        print(response.url)

    def parse_page(self, response):
        sel = response.selector
        meta = {key: sel.xpath(XPATHS[key]).extract()
                for key in ['speaker', 'title']}
        newurl = '%s/transcript?language=en' % response.url
        yield Request(newurl, callback=self.parse_transcript, meta=meta)

    def parse_transcript(self, response):
        print(response.url)

        item = TedTalkItem()
        sel = response.selector
        transcript = sel.xpath(XPATHS['transcript']).extract()
        transcript = [re.sub('\n+\t+', ' ', element) for element in transcript]
        transcript = [re.sub('\n+', ' ', element) for element in transcript]
        transcript = [re.sub('\t+', ' ', element) for element in transcript]
        transcript = [re.sub('\t+\n+', ' ', element) for element in transcript]
        item['speaker'] = response.meta['speaker']
        item['title'] = response.meta['title']
        item['transcript'] = transcript

        return item
