from scrapy.spider import Spider
from scrapy.selector import Selector
from tsnCrawler.items import TsncrawlerItem


class TsnSpider(Spider):
    name = "tsn"
    allowed_domains = ["tsn.ca"]
    start_urls = [
        "http://www.tsn.ca/nhl/scores/",
    ]

    def parse(self, response):
    
    	#get todays date
   # 	currentDate = datetime.datetime.now()
   # 	dateParam = "?date=%s/%s/%s" % (currentDate.month, currentDate.day, currentDate.year)
   # 	TsnSpider.start_urls[0]+=dateParam
   # 	print ("URL string:  %s", TsnSpider.start_urls[0])

    
        sel = Selector(response)
        sites = sel.xpath('//body/form/div/div/div/table/tbody')
        items = []
        for site in sites:
            item = BoxScoreCrawlerItem()
          #  item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('//tr/td/b/a/@href').extract()
          #  item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items