from scrapy.spider import Spider
from scrapy.selector import Selector
from gameCrawler.items import NhlcrawlerItem



class NhlSpider(Spider):
    name = "nhl"
    allowed_domains = ["nhl.com"]
    start_urls = ['http://www.nhl.com/ice/gamestats.htm']


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//body/div/div/div/div/table/tbody')
        items = []
        for site in sites:
        	#initialize crawler
            item = NhlcrawlerItem()
            
            #get date
            item['date'] = site.xpath('//tr/td//a/text()').extract()   

            # gather links
            item['link'] = site.xpath('//tr/td/a/@href').extract()
            items.append(item)
        return items