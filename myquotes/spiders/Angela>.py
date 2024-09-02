import scrapy
from ..items import MyquotesItem

class AngelaSpider(scrapy.Spider):
    name = "angela"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        mqi = MyquotesItem()
        for quote, author in zip(response.css('.text::text') , response.css('.author::text')):
            mqi['title'] = quote.extract()
            mqi['author'] = author.extract()

            yield {
                'title': mqi['title'],
                'author': mqi['author']
            }
