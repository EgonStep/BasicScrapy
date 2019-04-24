# -*- coding: utf-8 -*-
import scrapy


class EpisodesSpider(scrapy.Spider):
    name = 'episodes'
    allowed_domains = ['https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Breaking_Bad']
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Breaking_Bad']

    def parse(self, response):
        names = response.xpath('//table//td[@class="summary"]//text()').extract()
        for name in names:
            #yield return as object is created (preventing crash of memory)
            yield {'R':name}
    
