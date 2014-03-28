from scrapy.spider import Spider
from scrapy.selector import Selector
from gameCrawler.items import NhlcrawlerItem
from datetime import date, timedelta
import re
from scrapy.http import Request 


class NhlSpider(Spider):
    name = "nhl"
    allowed_domains = ["nhl.com"]
    #date passed as parameter for start url
    def __init__(self, seasonStart = None, seasonEnd = None, *args, **kwargs):
        super(NhlSpider, self).__init__(*args, **kwargs)
        season = seasonStart+seasonEnd
        print season
        ## TO DO: MULTIPLE SEASONS
    	self.start_urls = ['http://www.nhl.com/ice/gamestats.htm?season=%s' % season]


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath("//body/div/div/div/div/table[@class='data stats']/tbody")

        for site in sites:
        	#initialize crawler
            item = NhlcrawlerItem()
            #get date
            item['date'] = site.xpath('//tr/td//a/text()').extract()   
            # gather links
            item['link'] = site.xpath('//tr/td/a/@href').extract()
            yield item

		#get next page        
        nextPage = site.xpath("../tfoot/tr/td/div/div/a[contains(text(),'Next')]/@href").extract()
        #if there is a next page
        if(nextPage):
			nextPage = 'http://www.nhl.com' + nextPage[0]
			yield Request(nextPage, callback = self.parse)