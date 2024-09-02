import scrapy
from bs4 import BeautifulSoup
from ..items import My_faculty
import requests
class BiofacultyStanfordSpider(scrapy.Spider):
    name = "stanford"
    start_urls = [
        'https://biology.stanford.edu/people/faculty',
    ]

    def parse(self, response):
        abj = My_faculty()
        soup = BeautifulSoup(response.body, 'html.parser')
        names = soup.findAll('span')
        urls = soup.findAll('span')
        names = [name.text for name in names]
        urls = [url.find('a') for url in urls]
        for name,url in zip(names,urls):
            try:
                abj['name'] = name
                abj['url'] = url.get('href')
            except:
                continue
            yield {
                'names': name,
                'urls': url.get('href')
            }
        
        