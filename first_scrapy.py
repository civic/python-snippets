# -*- coding: utf-8 -*-
import scrapy


class FirstScrapySpider(scrapy.Spider):
    name = 'first_scrapy'
    allowed_domains = ['doc.scrapy.org']
    start_urls = ['https://doc.scrapy.org/en/latest/_static/selectors-sample1.html']

    def parse(self, response):
        for a in response.css('#images a'):
            yield {
                "href": a.css('::attr(href)').extract_first(),
                "name": a.css('::text').extract_first(),
            }

