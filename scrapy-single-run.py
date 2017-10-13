import scrapy
from scrapy.crawler import CrawlerProcess

class HatebuSpider(scrapy.Spider):
    name = 'hatebu_spider'
    start_urls = ['http://b.hatena.ne.jp/hotentry']
    custom_settings = {'DOWNLOAD_DELAY': 1}

    def parse(self, response):
        for entry in response.css('.entry-link'):
            print(entry.css('::text').extract_first())


if __name__ == "__main__":
    # spider 単独で実行できるようにする
    process = CrawlerProcess()
    process.crawl(HatebuSpider)
    process.start()

