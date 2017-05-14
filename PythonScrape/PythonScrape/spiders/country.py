# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from PythonScrape.items import PythonscrapeItem

class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
		Rule(LinkExtractor(allow='/index/', deny = '/user/'), follow = True),
		Rule(LinkExtractor(allow='/view/', deny = '/user/'), callback='parse_item')
    )

    def parse_item(self, response):
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
		item = PythonscrapeItem()
		name_css = 'tr#places_country_row td.w2p_fw::text'
		item['name'] = response.css(name_css).extract()
		pop_css = 'tr#places_population_row td.w2p_fw::text'
		item['population'] = response.css(pop_css).extract()
		return item
