import scrapy


class PropertySpiderSpider(scrapy.Spider):
    name = 'property_spider'
    allowed_domains = ['']
    start_urls = ['http:///']
    
    def parse(self, response):
        pass
