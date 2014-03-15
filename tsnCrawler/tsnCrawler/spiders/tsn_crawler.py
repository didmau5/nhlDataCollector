from scrapy.spider import Spider
from scrapy.selector import Selector
from tsnCrawler.items import TsncrawlerItem



class TsnSpider(Spider):
    name = "tsn"
    allowed_domains = ["tsn.ca"]
    
    #date passed as parameter for start url
    def __init__(self, date=None, *args, **kwargs):
        super(TsnSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.tsn.ca/nhl/scores/?date=%s' % date]


    def parse(self, response):
        
        sel = Selector(response)
        sites = sel.xpath('//body/form/div/div')
        items = []
        for site in sites:
        	#initialize crawler
            item = TsncrawlerItem()
            #gather links
            item['link'] = site.xpath('//div/div/div/div/p/a/@href').extract()
            items.append(item)
            	
            
        return items
