import scrapy

class SongsItem(scrapy.Spider):
    name = 'songs'
    start_urls = ['https://notjustok.com/category/mp3-songs/']

    def parse(self, response):
        for car in response.css('li.main-card-list'):
            yield{
                'name': car.css('h3::text').extract_first(),
                'type': car.css('a.card-meta-category::text').get()
            }
